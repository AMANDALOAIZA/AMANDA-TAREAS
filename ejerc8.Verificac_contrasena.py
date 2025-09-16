# 8. Verificación de Contraseña Simple

clave_prim = "Koko20"
usuario = input("Ingrese Usario: ")
contraseña = input("Ingrese Contraseña: ")
if clave_prim == contraseña:
    print ("Acceso Concedido Bienvenido: Sr.", usuario)
else:
    print("Acceso Denegado Sr.", usuario, "Vuelva a Intentarlo")