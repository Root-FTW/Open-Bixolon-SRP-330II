import serial

def abrir_cajon(port_name):
    # Comando de apertura del cajón de dinero en formato ESC/POS
    comando_cajon = b'\x1B\x70\x00\x19\xFF'

    # Abrir la conexión serial con la impresora
    try:
        impresora = serial.Serial(port_name, 9600, timeout=1)

        # Enviar el comando de apertura del cajón
        impresora.write(comando_cajon)

        # Cerrar la conexión serial
        impresora.close()

        print("Cajón abierto con éxito.")

    except Exception as e:
        print(f"Error al abrir el cajón: {e}")

if __name__ == '__main__':
    # Reemplaza 'COM3' por el nombre del puerto de tu impresora
    nombre_puerto = 'COM3'
    abrir_cajon(nombre_puerto)
