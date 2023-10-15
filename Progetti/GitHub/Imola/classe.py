import csv
import matplotlib.pyplot as plt
from adige import ArquivoCSV, limp, limp_csv

class AnalisiStelle:
    def __init__(self, csv_nome):
        self.csv_nome = csv_nome
        self.csv = ArquivoCSV(self.csv_nome)
        self.data = []

    def estrai_dati(self):
        catg = self.csv.extrair_coluna(4)
        catg = limp(catg)
        todos = self.cat_val(4, 0)
        data_str = todos

        for elemento in data_str:
            colore, temperatura = elemento.split("; ")
            self.data.append((colore.strip(), int(temperatura)))

    def calcola_medie(self):
        somme = {}
        conteggi = {}

        for colore, temperatura in self.data:
            if colore not in somme:
                somme[colore] = 0
                conteggi[colore] = 0
            somme[colore] += temperatura
            conteggi[colore] += 1

        medie = {colore: somma / conteggi[colore] for colore, somma in somme.items()}
        return medie

    def salva_dati(self, medie):
        limp_csv('./base.csv')

        with open('./base.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Color', 'Temperature'])

        with open(file='./base.csv', mode='a', encoding='utf8') as fp:
            for colore, media in medie.items():
                media = round(media)
                linha = str(colore) + ',' + str(media) + '\n'
                fp.write(linha)
                self.data.append(linha.strip())

    def ordina_dati(self):
        self.data.sort(key=lambda x: int(x.split(',')[1]), reverse=True)

    def stampa_dati(self):
        ordem = 0
        print('-------------------------- \n ')
        for x in self.data:
            x = x.strip().split(sep=',')
            ordem = ordem + 1
            print(f'{ordem}°  {x[0]}  --> temperatura de {x[1]}')

    def grafico(self):
        base_extrair = ArquivoCSV('./base.csv')
        cores = base_extrair.extrair_coluna(0)
        temperaturas = base_extrair.extrair_coluna(1)

        plt.bar(cores, temperaturas, color='blue')
        plt.plot()
        plt.show()

    def cat_val(self, cat:int, val:int) -> list:
        lista = []
        with open(file=self.csv_nome, mode='r', encoding='utf-8') as fp:
            line = fp.readline()
            line = fp.readline()
            while line:
                line = line.split(sep=',')
                p1 = line[cat]
                p2 = line[val]
                lista_x = p1 + '; ' + p2
                lista.append(lista_x)
                line = fp.readline()
        return lista


