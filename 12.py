#Calcula la potencia de un número
base = 2
exponente = 2


resultado_bucle = 1
for _ in range(exponente):
    resultado_bucle *= base
print(f"{base} elevado a {exponente} es: {resultado_bucle}") 