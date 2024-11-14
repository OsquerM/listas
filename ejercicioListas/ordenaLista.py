#Crea una funcion que ordene y retorne una matriz de numeros
#La funcion recibe una lista y un parametro adicional como "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#No se pueden utilizar funciones porpias del lenguaje que lo resuelvan automaticamente

def ordenar_matriz(matriz, orden):
    if orden == "Asc":
        # Ordena cada fila de la matriz en orden ascendente
        for fila in matriz:
            fila.sort()  # Ordena la fila de menor a mayor
    elif orden == "Desc":
        # Ordena cada fila de la matriz en orden descendente
        for fila in matriz:
            fila.sort(reverse=True)  # Ordena la fila de mayor a menor
    else:
        raise ValueError("El parámetro 'orden' debe ser 'Asc' o 'Desc'")
    
    return matriz




matriz = [5, 3, 8, 1]

# Ordenar la matriz de menor a mayor (ascendente)
matriz_asc = ordenar_matriz(matriz, "Asc")
print("Matriz ordenada de menor a mayor:")
for fila in matriz_asc:
    print(fila)

# Ordenar la matriz de mayor a menor (descendente)
matriz_desc = ordenar_matriz(matriz, "Desc")
print("\nMatriz ordenada de mayor a menor:")
for fila in matriz_desc:
    print(fila)