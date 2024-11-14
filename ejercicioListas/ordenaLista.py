#Crea una funcion que ordene y retorne una matriz de numeros
#La funcion recibe una lista y un parametro adicional como "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#No se pueden utilizar funciones porpias del lenguaje que lo resuelvan automaticamente

def ordenar_matriz(matriz, orden):
    if orden == "Asc":
        # Ordena toda la matriz (lista) en orden ascendente
        matriz.sort()  # Ordena la lista de menor a mayor
    elif orden == "Desc":
        # Ordena toda la matriz (lista) en orden descendente
        matriz.sort(reverse=True)  # Ordena la lista de mayor a menor
    else:
        raise ValueError("El parámetro 'orden' debe ser 'Asc' o 'Desc'")
    
    return matriz


# Definir una matriz unidimensional
matriz = [5, 3, 8, 1, 7, 2, 4, 6]

# Ordenar la matriz de menor a mayor (ascendente)
matriz_asc = ordenar_matriz(matriz, "Asc")
print("Matriz ordenada de menor a mayor:", matriz_asc)

# Ordenar la matriz de mayor a menor (descendente)
matriz_desc = ordenar_matriz(matriz, "Desc")
print("Matriz ordenada de mayor a menor:", matriz_desc)
