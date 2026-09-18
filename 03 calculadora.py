def soma():
    numero1 = int(input("Escolha um numero: "))
    numero2 = int(input("Escolha outro numero: "))
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} é igual a {resultado}")

def subtrair():
    numero1 = int(input("Escolha um numero: "))
    numero2 = int(input("Escolha outro numero: "))
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} é igual a {resultado}")

def multiplicar():
    numero1 = int(input("Escolha um numero: "))
    numero2 = int(input("Escolha outro numero: "))
    resultado = numero1 * numero2
    print(f"{numero1} * {numero2} é igual a {resultado}") 

def dividir():
    numero1 = int(input("Escolha um numero: "))
    numero2 = int(input("Escolha outro numero: "))
    resultado = numero1 / numero2
    print(f"{numero1} / {numero2} é igual a {resultado}")

while True:
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("0 - sair")

    opcao = input("Escolha uma opcao: ")


    if opcao == "1":
        soma()
    elif opcao == "2":
        subtrair()
    elif opcao == "3":
        multiplicar()
    elif opcao == "4":
        dividir()
    elif opcao == "0":
        print("Saindo do Sistema...")
        break
    else:
        print("opcao invalida, tente novamente!")

