
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import customtkinter as ctk  # Importamos CustomTkinter

# Parámetros
fs = 44100  # Frecuencia de muestreo (44.1 kHz)
t = np.linspace(0, 1, fs)  # Tiempo de 1 segundo

# Generar dos señales senoidales
f1 = 440  # Frecuencia de la primera señal (Hz) - Nota LA4
f2 = 660  # Frecuencia de la segunda señal (Hz) - Nota MI5

seno1 = np.sin(2 * np.pi * f1 * t)  # Primera onda
seno2 = np.sin(2 * np.pi * f2 * t)  # Segunda onda

# Suma de señales
suma_senales = (seno1 + seno2) / 2  # Normalizamos la amplitud

# Funciones para reproducir sonido
def play_seno1():
    sd.play(seno1, fs)

def play_seno2():
    sd.play(seno2, fs)

def play_suma():
    sd.play(suma_senales, fs)

# Configuración de la ventana principal con CustomTkinter
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema de color azul

ventana = ctk.CTk()
ventana.title("Reproductor de Señales de Audio")
ventana.geometry("400x300")  # Tamaño de la ventana
ventana.resizable(False, False)  # Bloqueamos el cambio de tamaño

# Título en la ventana
label = ctk.CTkLabel(ventana, text="Reproductor de Señales", font=("Arial", 18, "bold"))
label.pack(pady=15)

# Botones estilizados
btn_seno1 = ctk.CTkButton(ventana, text="🔊 Reproducir Señal 1 (440 Hz)", command=play_seno1, width=250)
btn_seno1.pack(pady=10)

btn_seno2 = ctk.CTkButton(ventana, text="🔊 Reproducir Señal 2 (660 Hz)", command=play_seno2, width=250)
btn_seno2.pack(pady=10)

btn_suma = ctk.CTkButton(ventana, text="🔊 Reproducir Suma de Señales", command=play_suma, fg_color="green", hover_color="darkgreen", width=250)
btn_suma.pack(pady=10)

# Mostrar la gráfica sin bloquear la GUI
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], seno1[:1000], label="Señal 1 (440 Hz)")
plt.plot(t[:1000], seno2[:1000], label="Señal 2 (660 Hz)")
plt.plot(t[:1000], suma_senales[:1000], label="Suma", linestyle='dashed')
plt.legend()
plt.title("Suma de Señales de Audio")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show(block=False)  # Mostrar la gráfica sin bloquear

# Iniciar la interfaz gráfica
ventana.mainloop()











