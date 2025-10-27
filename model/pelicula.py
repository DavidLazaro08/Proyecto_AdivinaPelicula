# Clase Película
# Con ella representamos una película o una serie del juego CineMaster.

from model.pista import Pista

class Pelicula:
    """ En esta clase guardamos la información básica de una película
    junto con algunas pistas asociadas para el modo de juego.
    """

    def __init__(self, titulo, genero="", anio=None):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.pistas = []

    # Métodos funcionales

    def agregar_pista(self, pista: Pista):
        """Añadimos una pista al listado"""
        self.pistas.append(pista)

    def mostrar_info(self):
        """Devolvemos un texto con los datos de la película y sus pistas."""
        info = f"{self.titulo} ({self.anio}) - {self.genero}\nPistas:"
        for i, pista in enumerate(self.pistas, start=1):
            info += f"\n  {i}. {pista.texto}"
        return info

    def __str__(self):
        return f"🎬 {self.titulo} ({self.anio}) - {self.genero}"
