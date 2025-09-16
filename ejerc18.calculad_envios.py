# 18 Calculadora de Costo de Envío

print ("Bienvenidos a zonaexports")
print ("Para envios a la zona Norte seleccione la opcion A")
print ("Para envios a la zona Sur seleccione la opcion B")
print ("Para envios a la zona Oeste seleccione la opcion C")
costo_zona_a = 15.00
costo_zona_b = 5.00
costo_zona_c = 10.00
peso = float (input ("Introduzca el peso: "))
zona = input ("Ingrese una zona A, B o C: ").upper()
costo_base = 0.00
descuento = 0.00
if zona == "A":
    costo_base = peso * costo_zona_a
    if peso < 10:
        descuento = costo_base * 0.10
elif zona == "B":
    costo_base = peso * costo_zona_b
    if peso < 20:
        descuento = peso * 0.15
elif zona == "C":
    costo_base = peso * costo_zona_c
    if peso < 25:
        descuento = peso * 0.20
else:
    print ("Zona de Envio no Valida")
costo_final = costo_base - descuento
print ("------>RESUMEN DE ENVIO<------")
print ("-------Peso del paquete: ", peso, "KG")
print ("-------Zona de Envio: ", zona)
print ("-------Costo de Envio: ", costo_base)
print ("-------Descuento aplicado: ", descuento)
print ("-------Costo Final: ", costo_final)
