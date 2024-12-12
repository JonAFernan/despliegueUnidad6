#Identificar si un número es par o impar
number = int(input("Introduce un numero entero: ")) #solicitamos un numero entero al usuario
# imprimimos el resultado en base al resultado del operador ternario
print (f"El número {number} es par" if number%2 == 0 else f"El número {number} es impar")