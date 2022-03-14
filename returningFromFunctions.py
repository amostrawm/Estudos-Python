def max(x, y):
    if x >= y:
        return x
    else:
        return y


print(max(4, 7))
print(max(4, 5))
z = max(5, 2)
print(z)
# -----------------------


def shortest_string(x, y):
    if len(x) <= len(y):
        return y
    else:
        return x


n = ["Olá"]
n2 = ["Olá bom dia"]
print(shortest_string(n, n2))

# qualquer codigo colocado depois de return não será executado!
def add_numbers(x, y):
    total = x + y
    return total
    print("it won't be printed")


print(add_numbers(4, 5))


