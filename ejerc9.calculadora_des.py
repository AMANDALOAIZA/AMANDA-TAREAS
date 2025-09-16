# 9. Calculadora de Descuento

precio = float (input("Ingrese el precio del producto: "))
if precio > 100:
    descuento = precio * 0.15
    total = precio - descuento
    print ("Su total es de: ", total)
else:
    print ("Su total es de: ", precio)