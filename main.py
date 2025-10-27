# Archivo principal del proyecto CineMaster

from controller.controller import Controller
from controller.datos_iniciales import cargar_datos_iniciales
from view.interfaz import Interfaz

if __name__ == "__main__":
    # Creamos el controlador (conexión con la base de datos y lógica)
    controller = Controller()

    # Cargamos datos de ejemplo si la base está vacía
    # Creamos esto pensando en darle sentido a la corrección de la actividad.
    cargar_datos_iniciales(controller)

    # Creamos la interfaz gráfica y le pasamos el controlador
    app = Interfaz(controller)

    # Iniciamos la aplicación
    app.iniciar()
