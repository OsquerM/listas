#Variable global 
chars = ""
#Funciones
def run(texts: list) -> list:
    # TODO
    global chars
    entrada = ["one","two","three"]
    chars = []
    for string in entrada:
        for caracter in string:
            chars.append(caracter)
    return chars


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(chars)