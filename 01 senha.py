nome = str(input("Qual o seu nome? "))
senha_digitada = str(input("Qual vai ser a sua senha: "))
senha_cadastrada = "123"
nome_cadastrado = "Ana"

while senha_digitada != senha_cadastrada or nome != nome_cadastrado:
    print("Senha ou nome incorreto! Tente novamente.")
    senha_digitada = input("digite sua senha: ")

print(f"{nome},Bem-Vindo ao Sistama...")