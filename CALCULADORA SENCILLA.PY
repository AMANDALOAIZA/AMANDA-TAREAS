print("CALCULADORA SIMPLE")

operacion = input ("elige la operacion que desea realizar (SUMA, RESTA, DIVISION, MULTIPLICACION)")

if operacion == "SUMA":
    numero_1 =float(input("ingrese el primer numero:"))
    numero_2 =float(input ("ingrese el segundo numero:"))

    resultado = numero_1 + numero_2

    print(f"el resultado de ña suma es : {resultado}") 

elif operacion == "RESTA":
     numero_3 =float(input("ingrese el primero valor"))
     numero_4 =float(input("ingrese el segundo valor"))

     resultado =numero_3 - numero_4

     print (f"el resultado de la resta es :{resultado}")

elif operacion == "MULTIPLICACION":
     numero_5 =float(input("ingrese el primer valor"))
     numero_6 =float(input("ingrese el segundo valor"))

     resultado =numero_5 * numero_6

     print (f"el resultado de la Multiplicacion es :{resultado}")

elif operacion =="DIVISION":
     numero_7 =float(input("ingrese primer valor"))
     numero_8 =float (input("ingrese el segundo valor"))

     resultado =numero_7 / numero_8

     print (f"el resultado de la division es :{resultado}")
     

