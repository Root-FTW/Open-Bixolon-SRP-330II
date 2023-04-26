# Abrir Cajón de Dinero con Impresora Bixolon SRP-330II

Este proyecto contiene un script en Python para abrir un cajón de dinero conectado a una impresora térmica Bixolon SRP-330II a través de un cable RJ11.

## Requisitos

- Python 3.x
- Biblioteca 'pyserial'

## Instalación

1. Clona el repositorio o descarga el código fuente.

```
git clone https://github.com/tu_nombre_de_usuario/abrir_cajon.git
```

2. Instala la biblioteca 'pyserial' si aún no la tienes instalada:

```
pip install pyserial
```

## Uso

1. Abre el archivo `abrir_cajon.py` en un editor de texto y modifica la variable `nombre_puerto` con el nombre del puerto de tu impresora:

```python
nombre_puerto = 'COM3'  # Reemplaza 'COM3' por el nombre del puerto de tu impresora
```

En Windows, el nombre del puerto suele ser "COMx" (donde x es un número). En Linux, podría ser "/dev/ttyUSBx" o "/dev/ttyACMx".

2. Ejecuta el archivo "abrir_cajon.py" desde la línea de comandos:

```
python abrir_cajon.py
```

Si todo funciona correctamente, deberías ver el mensaje "Cajón abierto con éxito" en la consola y el cajón de dinero conectado a la impresora Bixolon SRP-330II debería abrirse.

## Código

El script en Python utiliza la biblioteca 'pyserial' para enviar un comando ESC/POS a la impresora térmica Bixolon SRP-330II. El comando en formato ESC/POS utilizado para abrir el cajón es:

```
comando_cajon = b'\x1B\x70\x00\x19\xFF'
```

Este comando indica lo siguiente:

- `\x1B`: Carácter de escape (ESC).
- `\x70`: Comando de apertura del cajón (p).
- `\x00`: Selector del cajón de dinero (0 para el cajón 1, 1 para el cajón 2).
- `\x19`: Duración del pulso ON en milisegundos (decodificado en hexadecimal).
- `\xFF`: Duración del pulso OFF en milisegundos (decodificado en hexadecimal).

## Soporte

Si encuentras algún problema o tienes alguna pregunta, por favor crea un [nuevo issue](https://github.com/Root-FTW/Open-Bixolon-SRP-330II/issues) en el repositorio.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más información.
```
