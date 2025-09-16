# 14 Selección de Menú

print ("----___MENU DE OPCIONES___---")
print ("---OPCION 1 PIZZA--")
print ("---OPCION 2 HAMBURGUESA-")
print ("---OPCION 3 PERRO CALIENTE--")
while True:
 seleccion = int (input("Ingrese una opcion del 1 al 3: "))
 if seleccion <= 3:
  break
else:
 print ("Por Favor Ingrese una opcion Valida")

if seleccion == 1:
 print ("Tu opcion fue la opcion 1 : PIZZA ")
elif seleccion == 2:
 print ("Tu opcion fue la opcion 2 : HAMBURGUESA ")
else:
 print ("Tu opcion fue la opcion 3 : PERRO CALIENTE")
