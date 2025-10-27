# Carga inicial de datos de ejemplo para el proyecto CineMaster
# Desde aquí insertamos algunas películas y puntuaciones
# únicamente si la base de datos está vacía
# (Generadas por IA y pensando en la corrección de la actividad).

def cargar_datos_iniciales(controller):
    """Carga películas y puntuaciones de ejemplo si la base está vacía."""
    if not controller.gestor.listar_peliculas():
        print("📀 Cargando películas de ejemplo...")

        # Película 1
        controller.registrar_pelicula(
            "Matrix", "Ciencia ficción", 1999,
            ["Protagonizada por Keanu Reeves",
             "Dirigida por las hermanas Wachowski",
             "La píldora roja y la azul son clave en la trama"]
        )

        # Película 2
        controller.registrar_pelicula(
            "Titanic", "Romance / Drama", 1997,
            ["Dirigida por James Cameron",
             "La historia transcurre en un barco",
             "Leonardo DiCaprio y Kate Winslet son los protagonistas"]
        )

        # Película 3
        controller.registrar_pelicula(
            "Jurassic Park", "Aventura / Ciencia ficción", 1993,
            ["Dinosaurios clonados en una isla",
             "Dirigida por Steven Spielberg",
             "Basada en una novela de Michael Crichton"]
        )

        # Película 4
        controller.registrar_pelicula(
            "El Señor de los Anillos: La Comunidad del Anillo", "Fantasía / Aventura", 2001,
            ["Basada en la novela de J. R. R. Tolkien",
             "Dirigida por Peter Jackson",
             "Un anillo para gobernarlos a todos"]
        )

        # Película 5
        controller.registrar_pelicula(
            "Forrest Gump", "Drama / Comedia", 1994,
            ["Protagonizada por Tom Hanks",
             "Corre, Forrest, ¡corre!",
             "La vida es como una caja de bombones"]
        )

        # Película 6
        controller.registrar_pelicula(
            "Inception", "Ciencia ficción / Acción", 2010,
            ["Dirigida por Christopher Nolan",
             "Sueños dentro de sueños",
             "Protagonizada por Leonardo DiCaprio"]
        )

        # Película 7
        controller.registrar_pelicula(
            "Avatar", "Ciencia ficción / Aventura", 2009,
            ["Dirigida por James Cameron",
             "Planeta Pandora y los Na'vi",
             "Fue la película más taquillera durante años"]
        )

        # Ranking inicial
        controller.gestor.guardar_puntuacion("David Lázaro", 100, "2025-10-27 10:00")
        controller.gestor.guardar_puntuacion("Patricia", 85, "2025-10-26 17:20")
        controller.gestor.guardar_puntuacion("Pepe", 70, "2025-10-25 19:15")
        controller.gestor.guardar_puntuacion("Eva", 95, "2025-10-26 12:45")
        controller.gestor.guardar_puntuacion("Mari Paz", 70, "2025-10-24 18:30")

        print("Datos de ejemplo añadidos correctamente.")
        print("Base de datos lista para jugar.")
