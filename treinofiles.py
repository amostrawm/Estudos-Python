print("Para armazenar um nome digite [1]")
print("Para saber os nomes armazenados digite [2]")
decision = int(input())

if decision == 1:
    file = open("nomes.txt", 'w')
    print("Digite o nome: ")
    nome = input()
    file.writelines(nome)
    print("Nome " + nome + " armazenado com sucesso!")
    file.close()

elif decision == 2:
    file = open("nomes.txt", 'r')
    print("Nomes armazenados: ")
    print(file.read())
    file.close()

else:
    exit()