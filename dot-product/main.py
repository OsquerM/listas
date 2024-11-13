#Variable global
dprod = 0
#Funciones
def run(u: list, v: list) -> float | None:
    # TODO
    global dprod
    #Variable local
    for num1, num2  in zip(u, v):
        dprod += num1 * num2
        print(f"{num1} * {num2} el resultado es: {dprod}")
    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    
