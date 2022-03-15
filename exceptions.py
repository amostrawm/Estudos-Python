"""
Different exceptions are raised for different reasons.
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
"""

# num1 = 7
# num2 = 0
# print(num1 / num2)


"""
try/except
se houver algum erro de exception em try, o que estiver em except vai rodar. 
se o que estiver em run não apresentar erro de exception, o except não vai rodar.
exemplo:
"""
try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")
print("##################################")


"""
um bloco try pode ter varios exceptions.
um mesmo exceptions pode ter varias condições no mesmo bloco.
exemplo:
"""
try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")