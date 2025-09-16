# Ecuacion cuadratica

import cmath
print("Ingrese los coeficientes de la ecuación ax^2 + bx + c = 0")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = (b**2) - (4*a*c)


if discriminante > 0:
    
    x1 = (-b - discriminante**0.5) / (2*a)
    x2 = (-b + discriminante**0.5) / (2*a)
    print("\nHay dos soluciones reales:")
    print(f"x1 = {x1:.2f}")
    print(f"x2 = {x2:.2f}")
elif discriminante == 0:
    
    x = -b / (2*a)
    print("\nHay una sola solución real:")
    print(f"x = {x:.2f}")
else:
    
    sol1 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    sol2 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    print("\nNo hay soluciones reales (las soluciones son complejas):")
    print(f"x1 = {sol1}")
    print(f"x2 = {sol2}")