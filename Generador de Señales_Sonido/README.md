# Generador de Señales sonoras
En Python simulamos la suma de señales de audio usando NumPy y Matplotlib. También podemos reproducir el audio generado con sounddevice o scipy.io.wavfile.
 - Se definen las frecuencias de dos señales senoidales (440 Hz y 660 Hz).
 - Se generan las ondas senoidales con np.sin(2 * np.pi * f * t).
 - Se suman las señales y se normaliza la amplitud para evitar distorsión.
 - Se grafica la señal con Matplotlib para ver cómo se combinan las ondas.
 - Se reproduce el sonido usando sound device.
![Image](https://github.com/user-attachments/assets/6102cb03-027b-4d48-b27f-c48949e56893)
Agregamos una interfaz gráfica para poder escuchar la frecuencia 1 y 2, y la suma de ambas.
- ![Image](https://github.com/user-attachments/assets/d6ae6ee5-c6c5-44cb-baa5-a0db962c00a3)
