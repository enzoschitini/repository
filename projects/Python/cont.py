# Base de dados

propaganda_online = [
  {'tempo_gasto_site': 68.95, 'idade': 35, 'renda_area': 61833.90, 'tempo_gasto_internet': 256.09, 'cidade': 'Wrightburgh', 'pais': 'Tunisia', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 80.23, 'idade': 31, 'renda_area': 68441.85, 'tempo_gasto_internet': 193.77, 'cidade': 'West Jodi', 'pais': 'Nauru', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 69.47, 'idade': 26, 'renda_area': 59785.94, 'tempo_gasto_internet': 236.50, 'cidade': 'Davidton', 'pais': 'San Marino', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 68.37, 'idade': 35, 'renda_area': 73889.99, 'tempo_gasto_internet': 225.58, 'cidade': 'South Manuel', 'pais': 'Iceland', 'clicou_no_ad': 0},
  {'tempo_gasto_site': 88.91, 'idade': 33, 'renda_area': 53852.85, 'tempo_gasto_internet': 208.36, 'cidade': 'Brandonstad', 'pais': 'Myanmar', 'clicou_no_ad': 0},
  {'tempo_gasto_site': None, 'idade': 48, 'renda_area': 24593.33, 'tempo_gasto_internet': 131.76, 'cidade': 'Port Jefferybury', 'pais': 'Australia', 'clicou_no_ad': 1},
  {'tempo_gasto_site': 74.53, 'idade': 30, 'renda_area': 68862.00, 'tempo_gasto_internet': 221.51, 'cidade': 'West Colin', 'pais': 'Grenada', 'clicou_no_ad': 1},
  {'tempo_gasto_site': 69.88, 'idade': 20, 'renda_area': 55642.32, 'tempo_gasto_internet': 183.82, 'cidade': 'Ramirezton', 'pais': 'Ghana', 'clicou_no_ad': 0}
]

print('-------------------------------------------------------------------')
print("Lista dos usuários que clicaram na propaganda.")
print('\n')

# Estrutura de dados
leads = []
media_parcial = 0
total = 0
media = 0

# Busca 

for dado_de_usuario in propaganda_online:
  if dado_de_usuario['clicou_no_ad'] == 1:
    leads.append(dado_de_usuario['renda_area'])
    media_parcial = media_parcial + dado_de_usuario['renda_area']
    total = total + 1

print(leads)

# Média salarial

if total > 1:
  media = media_parcial / total
  print("Média salarial:", int(media))

print('\n')