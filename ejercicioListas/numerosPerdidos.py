#Dado un array de enteros ordenado y sin repetidos,
# crea una funcion que calcule y retorne todos los que faltan entre el mayor y el menor
#Lanza un error si el array de entrada no es correcto


numEnteros = [2,4,6,8]

def retornar():
    if len(numEnteros) < 2:
        raise ValueError("El numEnteros debe tener al menos dos números.")
    
    # Verificar que el numEnteros esté ordenado de menor a mayor
    for i in range(1, len(numEnteros)):
        if numEnteros[i] <= numEnteros[i - 1]:  # Si no está ordenado, lanzamos un error
            raise ValueError("El array debe estar ordenado de menor a mayor.")
    menor = numEnteros[0]
    mayor = numEnteros[-1]
    # Crear una lista de los números faltantes
    faltantes = []
    todos_los_numeros = list(range(menor, mayor +1))
    for numero in todos_los_numeros:
        if numero not in numEnteros:  # Si el número no está en el array original
            faltantes.append(numero)
        
    return faltantes
    

print(retornar())