nome = str(input("Qual o seu nome? "))

nota = float(input("Digite uma nota: "))

gostaria = str(input("Voce quer adicionar uma nota?(sim/nao): "))


cont = 1
while gostaria == "sim":
   nova_nota = float(input("Digite uma nota: "))
   nota = nova_nota + nota 
   gostaria = str(input("Voce quer adicionar uma nota?(sim/nao): "))
   cont +=1
media = nota / cont
if media < 5:
   print(f"{nome} voce foi reprovado e sua media foi {media}!")
else:
   print(f"{nome} voce foi aprovado e sua media foi {media}!")