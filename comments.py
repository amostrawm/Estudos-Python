x = 365
y = 7
# this is a comment

print(float(x % y)) # find the remainder
# print (x // y)
# another comment


# DOCSTRINGS
def shout(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")


shout("spam")


def bomdia(x, y):
    return x + " " + y


print(bomdia("Bom", "Dia"))