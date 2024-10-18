import pyautogui as pg  # Importar la librería 'pyautogui' para automatizar el control del mouse y teclado
import time

# Función para leer palabras desde un archivo y retornarlas junto con el contador de palabras
def leer_palabras_desde_archivo(archivo_nombre):
    contador_palabras = 0
    lista_palabras = []
    
    with open(archivo_nombre, 'r') as archivo:
        # Lee cada línea del archivo
        for linea in archivo:
            # Divide la línea en palabras usando split() y suma la cantidad de palabras
            palabras = linea.split()
            contador_palabras += len(palabras)
            # Agregar las palabras a la lista
            lista_palabras.extend(palabras)
    
    return contador_palabras, lista_palabras

# Función para enviar mensajes con pyautogui
def enviar_mensajes(contador_palabras, lista_palabras):
    '''Esperar 5 segundos antes de iniciar el envío de mensajes para dar tiempo 
    de abrir la ventana de WhatsApp o aplicación de mensajería'''
    time.sleep(5)

    # Bucle para enviar los mensajes la cantidad de veces que el usuario especificó
    for i in range(contador_palabras):
        # Escribir el mensaje en la aplicación con formato '1) mensaje', '2) mensaje', etc.
        pg.write(f'{lista_palabras[i]}')
        # Simular la pulsación de la tecla 'enter' para enviar el mensaje
        pg.press('enter')

# Llamada a las funciones
archivo_nombre = 'texto.txt'
contador_palabras, lista_palabras = leer_palabras_desde_archivo(archivo_nombre)
enviar_mensajes(contador_palabras, lista_palabras)






