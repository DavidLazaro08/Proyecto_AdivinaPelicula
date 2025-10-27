# Clase Controller
# Conecta la interfaz del juego CineMaster con la base de datos y la lógica interna.

# Basado en el ejercicio anterior "MixMaster" (simulador de cócteles).
# Se mantiene la misma estructura de controlador principal,
# adaptada al nuevo proyecto de cine "CineMaster".

from data.gestor_bd import GestorBD
from model.pelicula import Pelicula
from model.pista import Pista
from datetime import datetime


class Controller:
    """Controlador principal del juego 'Adivina la Película'.
    Desde aqí coordinamos las operaciones entre nuestra base y la interfaz.
    """

    def __init__(self):
        # Conexión a la base de datos
        self.gestor = GestorBD()
        # Lista temporal de películas cargadas en memoria
        self.peliculas = []

    # PELÍCULAS

    def cargar_peliculas(self):
        """Cargamos todas las películas"""
        self.peliculas = self.gestor.cargar_peliculas()
        print(f"{len(self.peliculas)} películas cargadas desde la base de datos.")
        return self.peliculas

    def registrar_pelicula(self, titulo, genero, anio, pistas):
        """Registramos una nueva película con sus pistas."""
        peli = Pelicula(titulo, genero, anio)
        for texto in pistas:
            peli.agregar_pista(Pista(texto))
        self.gestor.insertar_objeto_pelicula(peli)
        self.peliculas.append(peli)
        print(f"Película '{titulo}' registrada con {len(pistas)} pistas.")

    # JUEGO

    def obtener_pistas_pelicula(self, titulo):
        """Devolvemos las pistas de una película por su título."""
        for peli in self.peliculas:
            if peli.titulo.lower() == titulo.lower():
                return peli.pistas
        return []

    # PUNTUACIONES

    def guardar_puntuacion(self, jugador="Jugador", puntos=0):
        """Guardamos la puntuación del jugador (por defecto 'Jugador') con la fecha actual."""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.gestor.guardar_puntuacion(jugador, puntos, fecha)
        print(f"Puntuación guardada: {jugador} - {puntos} puntos")

    def obtener_ranking(self):
        """Devolvemos el ranking ordenado por puntuación."""
        return self.gestor.listar_puntuaciones()

    # UTILIDADES

    def limpiar_bd(self):
        """Eliminamos todos los registros de la base de datos (solo para pruebas)."""
        self.gestor.eliminar_todo()

    def cerrar(self):
        """Cerramos la conexión con la base de datos."""
        self.gestor.cerrar()
