# Clase GestorBD
# Se encarga de gestionar la base de datos SQLite.

# Me basé en el ejercicio anterior "MixMaster" (simulador de cócteles).
# Se aprovecha la misma estructura del gestor de base de datos SQLite,
# adaptada al nuevo proyecto de cine "CineMaster".

import sqlite3
from model.pelicula import Pelicula
from model.pista import Pista


class GestorBD:
    """ Gestiona las operaciones de base de datos:
        - Crear tablas
        - Guardar y leer películas, pistas y puntuaciones
    """

    # Nota: en el constructor utilicé 'row_factory' para poder acceder
    # a las columnas por nombre (por ejemplo, fila["titulo"]) en lugar de usar índices.
    # Es una mejora opcional respecto a la teoría que vimos en clase que encontré útil,
    # que no cambia el funcionamiento pero hace el código quizá más legible.

    def __init__(self, ruta_bd="data/db_cinemaster.db"):
        self.ruta_bd = ruta_bd
        self.conn = sqlite3.connect(self.ruta_bd)
        self.conn.row_factory = sqlite3.Row
        self._crear_tablas()

    # CREACIÓN DE TABLAS

    def _crear_tablas(self):
        cursor = self.conn.cursor()
        cursor.executescript("""
        CREATE TABLE IF NOT EXISTS peliculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT UNIQUE NOT NULL,
            genero TEXT,
            anio INTEGER
        );

        CREATE TABLE IF NOT EXISTS pistas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pelicula_id INTEGER NOT NULL,
            texto TEXT NOT NULL,
            FOREIGN KEY (pelicula_id) REFERENCES peliculas(id)
        );

        CREATE TABLE IF NOT EXISTS puntuaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            jugador TEXT NOT NULL,
            puntos INTEGER NOT NULL,
            fecha TEXT
        );
        """)
        self.conn.commit()
        print("Tablas creadas correctamente.")

    # GESTIÓN DE PELÍCULAS

    def insertar_pelicula(self, titulo, genero, anio):
        """Inserta una película si no existe y devuelve su id."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO peliculas (titulo, genero, anio)
            VALUES (?, ?, ?)
        """, (titulo, genero, anio))
        self.conn.commit()

        cursor.execute("SELECT id FROM peliculas WHERE titulo = ?", (titulo,))
        row = cursor.fetchone()
        return row["id"]

    def listar_peliculas(self):
        """Devuelve una lista con todas las películas registradas."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM peliculas")
        return [dict(row) for row in cursor.fetchall()]

    # GESTIÓN DE PISTAS

    def insertar_pista(self, pelicula_id, texto):
        """Inserta una pista asociada a una película."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO pistas (pelicula_id, texto)
            VALUES (?, ?)
        """, (pelicula_id, texto))
        self.conn.commit()

    def obtener_pistas_pelicula(self, pelicula_id):
        """Devuelve una lista de textos con las pistas de una película."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT texto FROM pistas
            WHERE pelicula_id = ?
            ORDER BY id ASC
        """, (pelicula_id,))
        return [row["texto"] for row in cursor.fetchall()]

    # GESTIÓN DE PUNTUACIONES

    def guardar_puntuacion(self, jugador, puntos, fecha):
        """Guarda una nueva puntuación en el historial."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO puntuaciones (jugador, puntos, fecha)
            VALUES (?, ?, ?)
        """, (jugador, puntos, fecha))
        self.conn.commit()

    def listar_puntuaciones(self):
        """Devuelve el ranking ordenado por puntuación."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT jugador, puntos, fecha
            FROM puntuaciones
            ORDER BY puntos DESC
        """)
        return [dict(row) for row in cursor.fetchall()]

    # Métodos que enlazan la base de datos con los objetos Pelicula y Pista.

    def insertar_objeto_pelicula(self, pelicula: Pelicula):
        """Inserta una película (objeto) junto con sus pistas."""
        pelicula_id = self.insertar_pelicula(
            pelicula.titulo, pelicula.genero, pelicula.anio
        )

        for pista in pelicula.pistas:
            self.insertar_pista(pelicula_id, pista.texto)

        print(f"🎬 Película '{pelicula.titulo}' y sus pistas registradas correctamente.")

    def cargar_peliculas(self):
        """Carga todas las películas con sus pistas en objetos Pelicula."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM peliculas")
        peliculas = []

        for fila in cursor.fetchall():
            peli = Pelicula(fila["titulo"], fila["genero"], fila["anio"])
            peli_id = fila["id"]

            cursor.execute("SELECT texto FROM pistas WHERE pelicula_id = ?", (peli_id,))
            for p in cursor.fetchall():
                peli.agregar_pista(Pista(p["texto"]))

            peliculas.append(peli)

        return peliculas

    def eliminar_todo(self):
        """Elimina todas las películas, pistas y puntuaciones (modo limpieza)."""
        cursor = self.conn.cursor()
        cursor.executescript("""
            DELETE FROM pistas;
            DELETE FROM peliculas;
            DELETE FROM puntuaciones;
        """)
        self.conn.commit()
        print("Base de datos limpia.")

    # CIERRE DE CONEXIÓN

    def cerrar(self):
        """Cierra la conexión con la base de datos."""
        self.conn.close()
        print("Conexión cerrada correctamente.")
