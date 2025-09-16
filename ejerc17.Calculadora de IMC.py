# Calculadora de IMC

peso = float (input ("Ingrese su peso: "))
altura = float (input ("Ingrese su Altura: "))
alturacuadrado = altura ** 2
imc = peso / alturacuadrado
if imc < 18.5:
    print ("Peso inferior al Normal")
elif imc >= 18.5 and imc <= 24.9:
    print ("Peso Normal")
elif imc >= 25.0 and imc <= 29.9:
    print ("Peso superior al Normal")
else:
    print ("Obesidad  es hora de hacer ejercicios y comer mas sano")