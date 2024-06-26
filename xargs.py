def suma(*numeros):
 resultado = 0

 for numero in numeros:
    resultado += numero

    print(resultado)

suma(5, 10, 15)
suma(5, 20)
suma(20, 3, 4, 5, 2)