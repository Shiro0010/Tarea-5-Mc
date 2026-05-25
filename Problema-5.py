# nombre: Manuel Alexander Chaux Buesaquillo.
# Grupo: 213022_499
# Programa: Ingenieria de Sistemas 
# 張り切っていこう!(Harikkite ikou!)
# Saludos a Kary y a emacs

# Para empezar vamos a definir una constante que marque el umbral de horas
UMBRAL_HORAS = 40

# Ahora definimos la matriz con sus datos
# Cada fila es: ["Nombre", Lunes, Martes, Miércoles, Jueves, Viernes]
matriz_datos = [
    ["Zenith Amane", 5, 8, 6, 8, 9],
    ["Karyme Hazel", 10, 8, 8, 7, 11],
    ["Tsukimi Akari", 8, 8, 8, 8, 8],
    ["Agnes Tachyon", 11, 6, 7, 8, 9]
]

'''Funcion que sumará las horas y clasificará la jornada según el umbral'''
def clasificar_jornada(fila):
    # Usamos una variable para gestionar mas facilmente la suma.
    horas = sum(fila[1:])

    # Esta parte de la funcion clasifica comparando el umbral con la suma obtenida
    if horas <= UMBRAL_HORAS:
        clasificacion = "Horario estándar"
    else:
        clasificacion = "Sobretiempo"
    
    # Retornamos los datos limpios cuando se cumple una de las condiciones (Nombre, Horas, Clasificación)
    return fila[0], horas, clasificacion


# Definimos un encabezado predeterminado y fijamos su espaciado
print(f"{'RECURSO':<15} | {'HORAS SEMANALES':<16} | {'CLASIFICACIÓN':<18}")
print("-" * 55)

# Con este ciclo for vamos a imprimir la tabla limpia
for recurso in matriz_datos:
    # Desempaquetamos lo que devuelve la función usando la variable del ciclo
    nombre, total_horas, jornada = clasificar_jornada(recurso)
    
    # Aquí hacemos la magia del alineado para que todo cuadre con el encabezado
    print(f"{nombre:<15} | {total_horas:<16} | {jornada:<18}")