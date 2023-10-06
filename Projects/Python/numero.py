def soma(a, b):
    return a + b

# Funções #########################################
###################################################

# Limpar uma lista - tirar valores repetidos
def limp(lista_limp : list) -> list:
    lista_limp = list(set(lista_limp))
    return lista_limp

# Limpar arquivo csv apagar tudo
def limp_csv(arquivo_csv : str):
   with open(file=arquivo_csv, mode='w') as file:
      file.write("")


# Extrair da celula um valor em uma posição
def extcel(lista_divd : list, elemento : int, simb : str, tipo : str) -> list:
   nova_lista = []
   for x in lista_divd:
      x = x.split(sep=simb)
      x = x[elemento]
      x = x.strip()
      if tipo == 'int':
         x = int(x)
         nova_lista.append(x)
      elif tipo == 'float':
         x = float(x)
         nova_lista.append(x)
      elif tipo == 'str':
         x = str(x)
         nova_lista.append(x)
   return nova_lista

# Media total
def media_de_lista(lista_media : list, round_num : int) -> float:
   from functools import reduce
   media = reduce(lambda x, y: x + y, lista_media) # Total
   media = media / len(lista_media) # Dividindo pela quantidade
   media = round(media, round_num)
   return media


def subtrair(a, b):
    return a - b

class Util(object):
   def __init__(self, nome) -> None:
      self.nome = nome
   
   def devid(self, num):
      num2 = num / 2
      return num2
