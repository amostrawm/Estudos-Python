#  Escrevendo algo no arquivo
#  O modo 'w' vai criar um arquivo se ele não existe ainda
file = open("newfile.txt", 'w')
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", 'r')
print(file.read())
file.close()

#  Se o arquivo for aberto de novo no modo 'w' 
#  todo o conteúdo do arquivo é deletado
file = open("newfile.txt", 'w')
file.write("All the content was deleted.")
file.close()

file = open("newfile.txt", 'r')
print(file.read())
file.close()

#  Usando o write como método ele retorna a quantidade de bytes
#  E também escreve o que foi pedido no argumento
msg = 'Hello world!'
file = open('newfile.txt', 'w')
amount_written = file.write(msg)
print(amount_written)
file.close()

file = open('newfile.txt', 'r')
print(file.read())
file.close()