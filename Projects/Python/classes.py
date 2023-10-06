from time import sleep

class Pessoa(object):

  def __init__(self, nome: str, idade: int, documento: str = None):
    self.nome = nome
    self.idade = idade
    self.documento = documento

  def dormir(self, horas: int) -> None:
    for hora in range(1,horas+1):
      print(f'Dormindo por {hora} horas')
      sleep(1)

  def falar(self, texto: str) -> None:
    print(texto)
  
  def maiuscolo(self) -> str:
    return self.nome.upper()
  
  def par(self) -> None:
    r = self.idade % 2
    if r == 0:
      print("Par", self.idade)
    else:
      print("Impar", self.idade)

  def __str__(self) -> str:
    return f'{self.nome}, {self.idade} anos e documento numero {self.documento}'

andre = Pessoa(nome='Andre Perez', idade=30, documento='123')
maria = Pessoa(nome='Maria Perez', idade=56, documento='456')
pedro = Pessoa(nome='Pedro Perez', idade=8)
enzo = Pessoa(nome='Enzo Schitini', idade=19, documento='2004')

print("-----------------------------")
# Não estão usando a classe
def maior_de_idade(idade: int) -> bool:
  return idade >= 18

if maior_de_idade(idade=enzo.idade):
  print(f'{enzo.nome} é maior de idade')
print("-----------------------------")

score_credito = {'123': 750, '456': 812, '789': 327, '2004': 444}

score = score_credito[enzo.documento]
print(score)

print(enzo.nome)
print("-----------------------------")
# Métodos - usam as classes

print(enzo)
enzo.falar(texto='Olá pessoal!')
print(enzo.maiuscolo())
enzo.par()