# 11 Año Bisiesto

año = int (input("Ingrese el Año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print ("Su año es Bisiesto")
else:
    print ("Su año no es Bisiesto")
    
    