salario = 1
salarioTotal = 0
for i in range(0, 24):
    print("Salario mês " + str(i+1) + " = " + str(salario))
    salarioTotal = salarioTotal + salario
    salario = salario * 2
    if i == 12:
        print("Total primeiro ano: " + str(salarioTotal))
print("Salário total: " + str(salarioTotal))