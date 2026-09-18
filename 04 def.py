def pares():
    numero = int(input("Quantos numeros pares voce quer? "))
    cont = 1
    valor_inicial = 0
    while cont <= numero:
        valor_inicial += 2
        print(f"{valor_inicial}")
        cont += 1
def impar():
    numero = int(input("Quantos numeros impares voce quer? "))
    cont = 1
    valor_inicial = -1
    while cont <= numero:
        valor_inicial += 2
        print(f"{valor_inicial}")
        cont +=1

def somatorio ():
    n1 = int(input("Escolha um numero pra usar o somatorio: "))
    n2 = n1
    while n1 > 0:
         n1 -= 1
         n2 = n2 + n1
    print(n2)

def fatorial ():
    n1 = int(input("Escolha um numero pra usar o fatorial: "))
    n2 = n1
    while n1 > 1:
        n1 -= 1
        n2 = n2 * n1
    print(n2)


while True:
    print("1 - Pares")
    print("2 - impares")
    print("3 - Somatorio")
    print("4 - Fatorial")
    print("0 - sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        pares()
    elif opcao == "2":
        impar()
    elif opcao == "3":
        somatorio()
        break
    elif opcao == "4":
        fatorial()
        break
    elif opcao == "0":
        print("Saindo do Sistema...")
        break
    else:
        print("opcao invalida, tente novamente!")
        break
