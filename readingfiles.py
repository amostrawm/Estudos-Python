#  O conteúdo de um arquivo pode ser lido com o metodo read
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()
#  Aqui ele printa todo o conteúdo que está dentro do arquivo

#  Para ler uma certa quantidade do arquivo pode colocar argumentos
#  no read como no exemplo
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

file = open("filename.txt", "r")
str = file.read()
print(len(str))
file.close()

#  Aqui ele printa em forma de lista todas as linhas do arquivo
file = open("filename.txt", "r")
print(file.readlines())
file.close()

#  Aqui nesse loop ele printa todas as linhas também
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close() 