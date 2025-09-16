

registros_estudiantiles = [
    ('rafael', 'Matemáticas', 98, 95),
    ('valentin', 'Física', 65, 88),  
    ('amanda', 'Química', 92, 75),  
    ('beatriz', 'Historia', 85, 90),  
    ('armando', 'Arte', 55, 60)      
]
aprobados = []
reprobados = []
cuadro_de_honor = []
for registro in registros_estudiantiles:
    nombre, materia, calificacion, asistencia = registro

    # Lógica condicional
    if asistencia < 80:
        reprobados.append(nombre)
    elif calificacion < 70:
        reprobados.append(nombre)
    elif calificacion >= 95:
        cuadro_de_honor.append(nombre)
        aprobados.append(nombre)
    else:
        aprobados.append(nombre)

print("Reporte de Calificaciones")
print(f"Estudiantes en el Cuadro de Honor: {cuadro_de_honor}")
print(f"Estudiantes Aprobados: {aprobados}")
print(f"Estudiantes Reprobados: {reprobados}")