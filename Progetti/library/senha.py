minha_senha = '14'

def verificar_senha(nova_senha):
    if len(nova_senha) > 6:
        print("OK")
    else:
        print("No")
