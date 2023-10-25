import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
from functools import reduce

from adige import valore_abbreviato
from adige import ArquivoCSV

index_csv = './index.csv'

df = pd.read_csv(index_csv, na_values='na')

struttura = df.shape
struttura = str(struttura).replace('(', '').replace(')', '')
struttura = str(struttura).strip().split(sep=',')
print(f'Data information: {valore_abbreviato(struttura[0])} lines and {valore_abbreviato(struttura[1])} columns.')
    
df.dtypes
df.select_dtypes('object').describe().transpose()
df.drop('Country', axis=1).select_dtypes('number').describe().transpose()
df.isna().any()

def stats_dados_faltantes(df: pd.DataFrame) -> None:

  stats_dados_faltantes = []
  for col in df.columns:
    if df[col].isna().any():
      qtd, _ = df[df[col].isna()].shape
      total, _ = df.shape
      dict_dados_faltantes = {col: {'quantity': qtd, "percentage": round(100 * qtd/total, 2)}}
      stats_dados_faltantes.append(dict_dados_faltantes)

  for stat in stats_dados_faltantes:
    print(stat)

stats_dados_faltantes(df=df)

from adige import ArquivoCSV
csv = ArquivoCSV('./index.csv')
csv = csv.extrair_coluna(0)
print(f'Numero iniziale: {len(csv)}')

def pulizia(archivio):
    file = []
    with open(file=archivio, mode='r', encoding='utf-8') as fp:
        line = fp.readline()
        line = fp.readline()
        while line:
            line_sep = line.split(sep=',')
            if line_sep[3] != '':
                file.append(line)
                line = fp.readline()
            else:
                line = fp.readline()
    from adige import limp_csv
    limp_csv(archivio)

    with open(file=archivio, mode='a', encoding='utf-8') as fp:
        fp.write('Country,iso3c,year,Overall Scores,Safety and Security,Ongoing Conflict,Militarian')
        for x in file:
            fp.write(x)

pulizia('./index.csv')
csv = ArquivoCSV('./index.csv')
csv = csv.extrair_coluna(0)
print(f'Numero finale: {len(csv)}')

def cattegorie(file, colonna:int):
    csv = ArquivoCSV(file)
    lista = list(set(csv.extrair_coluna(colonna)))
    return list(filter(None, lista))

print(f'I dati vanno dal {min(cattegorie(index_csv, 2))} fino a {max(cattegorie(index_csv, 2))}, tutto sommato: {len(cattegorie(index_csv, 2))} anni di analise.')

paese_nome = 'Italy'

def trovare_paese(paese:str) -> list:
    paesi = []
    with open(file=index_csv, mode='r', encoding='utf-8') as fp:
        line = fp.readline()
        line = fp.readline()
        while line:
            line = line.strip()
            line_x = line.split(sep=',')
            if line_x[0] == paese:
                paesi.append(line)
                line = fp.readline()
            else:
                line = fp.readline()
    return paesi

print(trovare_paese(paese_nome))
print(len(trovare_paese(paese_nome)))
trovare_paese(paese_nome)[0]

def calcoli_paese(paesi:list):

    overall_scores = []
    safety_security = []
    ongoing_conflict = []
    militarian = []

    for x in paesi:
        x = str(x)
        x_sep = x.split(sep=',')
        overall_scores.append((x_sep)[3])
        safety_security.append((x_sep)[4])
        ongoing_conflict.append((x_sep)[5])
        militarian.append((x_sep)[6])
    
    return overall_scores, safety_security, ongoing_conflict, militarian

overall_scores = calcoli_paese(trovare_paese(paese_nome))[0]
print(overall_scores)

def informazioni_paese(paese:str):
    # Gli anni
    anni = list(map(int, cattegorie(index_csv, 2)))
    anni.sort()
    print(anni) 
    # Dati prelevati
    overall_scores = list(map(float, calcoli_paese(trovare_paese(paese))[0]))
    safety_security = list(map(float, calcoli_paese(trovare_paese(paese))[1]))
    ongoing_conflict = list(map(float, calcoli_paese(trovare_paese(paese))[2]))
    militarian = list(map(float, calcoli_paese(trovare_paese(paese))[3]))
    print(overall_scores)
    # Le medie
    overall_scores_media = round(reduce(lambda x, y: x + y, overall_scores) / len(anni), 2)
    safety_security_media = round(reduce(lambda x, y: x + y, safety_security) / len(anni), 2)
    ongoing_conflict_media = round(reduce(lambda x, y: x + y, ongoing_conflict) / len(anni), 2)
    militarian_media = round(reduce(lambda x, y: x + y, militarian) / len(anni), 2)
    medie = [paese, overall_scores_media, safety_security_media, ongoing_conflict_media, militarian_media]
    print(f'Le medie di {paese} sono: \nPontuação geral: {overall_scores_media} \nSegurança e proteção: {safety_security_media} \nConflito contínuo: {ongoing_conflict_media}  \nMilitar: {militarian_media}.')

    return medie

informazioni_paese('Italy')

data = trovare_paese(paese_nome)
data.sort(key=lambda x: float(x.split(',')[2]), reverse=True)

ordem = 0
print('------------------------------------------')
for x in data:
    x = x.strip().split(sep=',')
    ordem = ordem + 1
    print(f'{ordem}° {x[0]} - {x[2]}  --> Overall Scores {x[3]}')
    print('------------------------------------------')

def creando_grafico_paese(paese:str, nome_grafico:str):
    anni = list(map(int, cattegorie(index_csv, 2)))
    anni.sort()

    overall_scores = list(map(float, calcoli_paese(trovare_paese(paese))[0]))
    safety_security = list(map(float, calcoli_paese(trovare_paese(paese))[1]))
    ongoing_conflict = list(map(float, calcoli_paese(trovare_paese(paese))[2]))
    militarian = list(map(float, calcoli_paese(trovare_paese(paese))[3]))

    x  = anni
    y1 = overall_scores
    y2 = safety_security
    y3 = ongoing_conflict
    y4 = militarian

    #plt.title(f'Indice di pace globale 2023 in {paese}')
    plt.plot(x, y1, color = "green", label="overall_scores")
    plt.plot(x, y2, color = "blue", label="safety_security")
    plt.plot(x, y3, color = "orange", label="ongoing_conflict")
    plt.plot(x, y4, color = "red", label="militarian")
    #plt.xlabel("Anni")
    #plt.ylabel("Punteggi")
    plt.savefig(nome_grafico)
    plt.legend()
    plt.show()

creando_grafico_paese(paese=paese_nome, nome_grafico=paese_nome)

def medie_paesi_periodo():
    paesi = cattegorie(index_csv, 0)
    print(paesi)
    tutti = []
    for x in paesi:
        tutti.append(informazioni_paese(paese=x))
    return tutti

def lista_string():
   tutti = medie_paesi_periodo()
   lista = []
   for x in tutti:
      x = [str(elemento) for elemento in x]
      stringa = '/ '.join(x)
      lista.append(stringa)
      #print(stringa)
   return lista

lista = lista_string()
print(lista)

# Gruppetto dei cinque

data = lista_string()
print(data)

# Ordina i dati in base alla temperatura (dal più alto al più basso)
data.sort(key=lambda x: float(x.split('/')[1]), reverse=False)

def ordinando(data:list):
   ordine = 0
   paesi_in_ordine = []
   print(' \n ')
   print('--------------------------')
   for x in data:
      ordine = ordine + 1
      add = x + '/ ' + str(ordine)
      x = x.strip().split(sep='/')
      print(f'{ordine}° {x[0]} --> Overall Scores {x[1]}')
      paesi_in_ordine.append(add)
   #print(paesi_in_ordine)
   print('--------------------------')
   return paesi_in_ordine

ordinando(data)

def smistando(data:list):

   tre_primi = []
   tre_ultimi = []

   tre_primi.append(data[3])
   tre_primi.append(data[4])
   tre_primi.append(data[5])
   tre_ultimi.append(data[-5])
   tre_ultimi.append(data[-6])
   tre_ultimi.append(data[-7])

   return tre_primi, tre_ultimi


paesi_in_ordine = ordinando(data)
print(smistando(paesi_in_ordine)[0])
print(smistando(paesi_in_ordine)[1])

def media_generale(cosa:int, lista):
   dati = lista
   data = []
   for i in dati:
      i_sep = i.split(sep='/')
      i = float(i_sep[cosa].strip())
      data.append(i)
   media = round(reduce(lambda x, y: x + y, data) / float(len(data)), 2)
   print(f'Valore maggiore: {max(data)} e minimo valore: {min(data)} -> Media: {media}')

print('Global')
print('Overall score:')
media_generale(1, data)
print('Security and protection')
media_generale(2, data)
print('Continuing conflict')
media_generale(3, data)
print('Military')
media_generale(4, data)

# Grafico dei tre primi e dei tre ultimi

#paesi_in_ordine = ordinando(data)

primi = smistando(paesi_in_ordine)[0]
ultimi = smistando(paesi_in_ordine)[1]
print(primi)
print(ultimi)

nomi = []

for x in primi:
    x_sep = x.split(sep=('/'))
    nomi.append(x_sep[0])
for x in ultimi:
    x_sep = x.split(sep=('/'))
    nomi.append(x_sep[0])

for i in nomi:
    #print(i)
    creando_grafico_paese(i, i)