#  Tipo de Triángulo

lado1 = float (input("Ingrese medida del primer lado: "))
lado2 = float (input("Ingrese medida del segundo lado: "))
lado3 = float (input("Ingrese medida del tercer lado: "))
if lado1 == lado2 and lado2 == lado3:
    print("Su triangulo es Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print ("Su triangulo es Isoseles")
else:
    print ("Su triangulo es Escaleno") 