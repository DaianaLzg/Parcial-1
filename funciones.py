# Esta función carga datos en una matriz
# (Número de historia clínica (un número entero). Nombre del paciente (una cadena de texto). Edad del paciente (un número entero). Diagnóstico (una cadena de texto). Cantidad de días de internación (un número entero).)
def carga_de_datos():
    matriz = []
    cantidad_ingresados = int(input("¿Cuantos pacientes desea ingresar?: "))
    pacientes_cargados = 0
    while pacientes_cargados < cantidad_ingresados:
        numero_historia = int(input("Ingrese número de historia clínica (un número entero): "))
        nombre_paciente = str(input("Ingrese el nombre del paciente: "))
        edad_paciente = int(input("Ingrese edad del paciente: "))
        diagnostico_paciente = str(input("Ingrese diagnostico del paciente: "))
        dias_de_internacion = int(input("Ingrese cantidad de dias de internacion: "))
        pacientes_cargados += 1
        paciente = [numero_historia,nombre_paciente,edad_paciente,diagnostico_paciente,dias_de_internacion]
        matriz += [paciente]
    return matriz

# Esta función, dado el número de historia clínica de un paciente, busque en la lista y muestre todos los datos de dicho paciente
def buscar_por_historial(matriz, numero_historia):
    for paciente in matriz:
        if paciente[0] == numero_historia:
            break
    return paciente


# Ordenar pacientes por número de historia clínica.
def ordenar_por_historial(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[j][0] > matriz[j+1][0]: #
                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]
    return matriz

# Mostrar Paciente con mas días de internación
def paciente_mas_internacion(matriz):
    mas_internacion = matriz[1]
    for paciente in matriz:
        if paciente[4] > mas_internacion[4]:
            mas_internacion = paciente
    return mas_internacion

# Mostrar Paciente con menos días de internación
def paciente_menos_internacion(matriz):
    menos_internacion = matriz[1]
    for paciente in matriz:
        if paciente[4] < menos_internacion[4]:
            menos_internacion = paciente
    return menos_internacion

# Mostrar cantidad de pacientes con mas de 5 días de internación
def paciente_mayores_a_5_dias_internacion(matriz):
    mas_de_5_dias = []
    for paciente in matriz:
        if paciente[4] > 5:
            mas_de_5_dias += [paciente]
    return mas_de_5_dias

#Promedio de dias de internacion de todos los pacientes
def promedio_dias_de_internacion(matriz: list[4]):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[4]    
    resultado = suma / len(matriz)
    return resultado

