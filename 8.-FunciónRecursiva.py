#Intenta cambiar el código para calcular el factorial de otro número, como 7.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"El factorial de 7 es: {factorial(7)}")
