print(int(3.2))
print(float(10))
print(complex(1))

nome = "Ess"
nome2 = "DDD"
print("Resposta: " + nome + ' ' + nome2 + ".")
print(f'Resposta: {nome} {nome2}.')

email = 'enzo@gmail.com'
print('0: ' + email[0])
print('11: ' + email[11])
print('-1: ' + email[-1])
print('-2: ' + email[-2])
email_usuario = email[0:4]
print(email_usuario)
email_provedor = email[5:14]
print(email_provedor)

# Metodos

print("####################################################")
endereco = "Avenida, 145, Rio, Rio, Brasil"
print(endereco.upper())
posicao = endereco.find("Avenida")
print(posicao)
print(endereco.replace("Avenida", "Av"))

# Conversão

print("####################################################")
idade = 19
print(type(idade))
idade = str(idade)
print(type(idade))
faturamento = "R$ 35 mil"
print(faturamento)
print(type(idade))
faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))

# Conversão

lat = "-22.005320"
lon = "-47.891040"
latlon = "-22.005320;-47.891040"
print("####################################################")
posicao_char_divisao = latlon.find(';')
print(posicao_char_divisao)

lat_startup = latlon[0:posicao_char_divisao]
print(lat_startup)

lon_startup = latlon[posicao_char_divisao+1:len(latlon)]
print(lon_startup)

# Boleanos

print("####################################################")
verdadeiro = True
print(verdadeiro)
falso = False

print(falso)
print(type(True))

saldo_em_conta = 200
valor_do_saque = 100

pode_execultar_saque = valor_do_saque <= saldo_em_conta
print(pode_execultar_saque)
print("------------")
# OU = |
print(True | True)
print(True | False)
print(False | False)
print(False | True)
print("------------")
# E = &
print(True & True)
print(True & False)
print(False & False)
print(False & True)
print("------------")
print(not True)
print(not False)