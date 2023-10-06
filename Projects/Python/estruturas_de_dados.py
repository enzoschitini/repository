# Lista de filmes
print('---------------------------------------')
filmes = ['1. As asas da liberdade', '2. O Poderoso Chefão', '3. O Cavaleiro das Trevas', '4. O Poderoso Chefão - Parte II', '5. A palavra aos jurados', '6. Lista de Schindler', '7. O Senhor dos Anéis - O Retorno do Rei', '8. Pulp Fiction', '9. O Senhor dos Anéis - A Sociedade do Anel', '10. O bom, o mau, o mau']
print("### Lista original:")
print(filmes)

# Métodos
print('---------------------------------------')

# Insira um filme no início da lista
filmes.insert(0, '1. A vida é bela')
print("### Lista modificada:")
print(filmes)

print('---------------------------------------')

# Remova o segundo filme da lista e imprima-o
filmes_update = filmes.pop(1)

# Substitua o filme removido por '' na lista
filmes[1] = filmes[1].replace(filmes_update, '')
print("### Final:")
print(filmes)