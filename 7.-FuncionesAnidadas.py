#Modifica el código para que la función interior reciba un parámetro y lo imprima.

def funcion_exterior():
    def funcion_interior(mensaje):
        print(f"Mensaje de la función interior: {mensaje}")
    funcion_interior("¡Hola desde la función interior!")
    print("Esta es la función exterior")

funcion_exterior()
