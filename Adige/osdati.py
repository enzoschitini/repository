def prelevando_dati(url:str, archivo:str):

   import pandas as pd
   from time import sleep

   with open(file=archivo, mode='w') as file:
      file.write("")
   
   df = pd.read_csv(url)

   intestazioni = df.head(n=0)
   intestazioni = list(intestazioni)
   intestazioni = str(intestazioni)
   x = intestazioni
   x = x.replace('[', '').replace(']', '').replace("'", '').replace(' ', '')

   with open(file=archivo, mode='w') as file:
      file.write("")
      file.write(x + '\n')
   
   lista = df.values.tolist()

   with open(file=archivo, mode='a', encoding='utf-8') as fp:
      for x in lista:
         x = str(x)
         x = x.replace('[', '').replace(']', '').replace("'", '').replace(' ', '')
         fp.write(x + '\n')
         sleep(0.0005)


URL = 'https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/develop/dataset/credito.csv'

prelevando_dati(url=URL, archivo='./base.csv')