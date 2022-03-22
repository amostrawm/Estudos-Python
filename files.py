#  Função para abrir arquivos
myfile = open("filename.txt")

#  Podemos definir o modo de como vamos abrir o arquivo
#  colocando um segundo argumento na função open
#  'r' entra como modo read, 'w' entra como write
#  'a' entra como apend, pra adicionar conteudos no final do arquivo
#  adicionando 'b' abre como binario, que é usado pra arviso non-text
#  como imagens e arquivos de som

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")
print("Closing the file")
myfile.close()

#  Adicionar r+ abre o arquivo como writing e  reading