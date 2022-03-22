#  Raising Exceptions
#  Traz um erro, levanta um erro e apresenta 

print(1)
print(2)
# ############

name = '123'
# raise NameError('Invalide name!')
#  Aqui eu consigo nomear um erro e apresentar.

#  Dentro dos blocos except pode chamar um raise e ele vai
#  apresentar qualquer erro que aconteça no bloco

try:
    num = 5 / 0
except:
    print("An error ocurred")
    raise