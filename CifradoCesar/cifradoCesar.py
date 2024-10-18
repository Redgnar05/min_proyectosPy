"""Este módulo contiene funciones para codificar y decodificar mensajes 
usando un cifrado César. 

El cifrado César es un método de cifrado de sustitución donde cada letra 
en el texto se reemplaza por otra letra que se encuentra un número fijo 
de posiciones más adelante en el alfabeto. Este módulo proporciona 
funciones para obtener la posición de una letra en el alfabeto y 
convertir una posición de vuelta a una letra, además de realizar 
la codificación y decodificación según un desplazamiento dado.
"""

def obtener_posicion(letra):
    """Obtiene la posición de una letra en el alfabeto (A = 1, B = 2, ..., Z = 26).
    Args:
        letra (str): Una letra mayúscula del alfabeto.
    Returns:
        int: La posición de la letra en el alfabeto.
    """
    return ord(letra) - ord('A') + 1

def desplaza(posicion):
    """Convierte una posición numérica de vuelta a una letra del alfabeto.
    Args:
        posicion (int): La posición numérica de la letra (1 a 26).
    Returns:
        str: La letra correspondiente a la posición dada.
    """
    return chr(posicion + ord('A') - 1)


# Leer las entradas del usuario
desplazamiento = int(input("Digite el número de desplazamiento: "))
mensaje = input("Digite el mensaje: ").upper()  # Convertir el mensaje a mayúsculas
vector = []
codificado = ""

# Leer la acción del usuario
accion = input('Digite -> C: para codificar, Digite -> D: para decodificar: ').upper()

# Validar la acción del usuario
if accion not in ['C', 'D']:
    print("Acción inválida. Por favor, elige 'C' o 'D'.")
else:
    for caracter in mensaje:
        if caracter.isalpha():  # Verificar si es una letra
            n = obtener_posicion(caracter)
            
            # Aplicar el desplazamiento dependiendo de la acción
            if accion == 'C':
                n = n + desplazamiento  # Codificar
            elif accion == 'D':
                n = n - desplazamiento  # Decodificar

            # Ajustar si se sale del rango (1-26)
            n = (n - 1) % 26 + 1

            # Convertir la nueva posición a la letra correspondiente
            vector.append(desplaza(n))
        else:
            vector.append(caracter)  # Mantener caracteres no alfabéticos intactos

    # Unir la lista de caracteres en un string final
    codificado = ''.join(vector)
    print(f"Resultado: {codificado}")



