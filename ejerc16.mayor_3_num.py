# 16  El Mayor de Tres Números

num1 = float (input("Ingrese primer numero: "))
num2 = float (input("Ingrese segundo numero: "))
num3 = float (input("Ingrese tercer numero: "))
if num1 > num2 and num1 > num3:
    print ("El numero mayors es: ", num1)
elif num2 > num1 and num2 > num3:
    print ("El numero mayor es: ", num2)
else:
    print ("El numero mayor es: ", num3)