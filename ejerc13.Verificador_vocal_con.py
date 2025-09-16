# 13 Verificador de Vocal o Consonante

print ("Vocales o Consonantes")
while True:
 caracter = input ("Ingrese una Letra:")
 if len(caracter) == 1:
    break
 else:
   print ("Ingrese solamente un caracter intente de nuevo")

caracter_min = caracter.lower()
vocales = "aeiou"
if caracter_min in vocales:
    print ("Su letra es la vocal", caracter)
else:
 print ("Su letra es la consonante", caracter)