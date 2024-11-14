#Simula el funcionamiento de una maquina expendedora creando una operacion que reciba dinero, y un numero que indique la seleccion del producto
# -El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor número de monedas)
#- Si el dinero es insuficiente o el numero de producto no existe, deberá indicarse con un mensaje y retornar todas las monedas.
#- Si no hay dinero de vuelta, el array se retornará vacío
#- Para que resulte mas simple, trabajaremos en centimos con monedas de 5 , 10 , 50 , 100 y 200
#- Debemos controlar las menodas enviadas estén dentro de las soportadas.


dinero = 5000
productos = ["cocacola", "agua", "fanta","nestea"]
precio = [100,50,200,5]

salida = True
productosComprados = []

while salida:
    print("Bienvenido a la máquina expendedora, productos disponibles \n-cocacola\n -agua \n -fanta \n -nestea")
    eleccion = input("Selecciona el producto: ").lower()
    if eleccion not in productos:
        print("Producto no valido")
        continue

    indiceProducto = productos.index(eleccion)
    costeProducto = precio[indiceProducto]
    if dinero >= costeProducto:
        dinero -= costeProducto
        productosComprados.append(eleccion)
        print(f"Has comprado {eleccion}. Te quedan {dinero} céntimos.")
        salida = False  
        print(f"Productos comprados: {productosComprados}")

    else:
        print(f"Dinero insuficiente para comprar {eleccion}. Te quedan {dinero} céntimos.")
        salida = False 

    continuar = input("¿Quieres seguir comprando?: s/n: ").lower()
    if continuar == "s":
        salida = True

print("Resumen de las compras: ")
for producto in productosComprados:
    print(f"- {producto}")