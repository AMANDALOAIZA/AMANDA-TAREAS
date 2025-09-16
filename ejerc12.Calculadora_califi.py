# Calculadora de Calificaciones

nota = int (input("Ingrese la nota del estudiante entre 0-100: "))
if nota >= 80:
    print ("Su nota es A")
elif nota >= 60:
    print ("Su nota e B")
elif nota >= 40:
    print ("Su nota es C")
elif nota >= 20:
    print ("Su nota es D")
else:
    print ("Su nota es F REPROBADO")