#  Assert testa uma expressão e se ela for falsa,
#  uma exception é chamada
print(1)
assert 2 + 2 == 4
print(2)
#  assert 1 + 1 == 3
print(3)

temp = -10
#  assert (temp >= 0) , "Colder than absolute zero!"
#  Pode colocar um segundo argumento no assert pra apresentar o erro


#  Uma função que testa se o valor de X é positivo
def my_func(x):
    assert x > 0, "Error!"
    print(x)

