nome = input("Digite seu nome: ")
idade = int(input("Digite sua Idade: "))

print("Seu nome é " + nome + "\nVocê têm " + str(idade))

if idade >= 18:
    print("Você já é maior de idade!")
else: 
    print("Você ainda é menor de idade!")