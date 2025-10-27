# Clase Pista
# Con ella representamos una pista asociada a una película.

class Pista:
    """ En esta clase guardamos el texto de una pista
    que servirá como ayuda para adivinar la película.
    """

    def __init__(self, texto):
        self.texto = texto

    def __str__(self):
        """Mostramos la pista cuando se imprime el objeto."""
        return f"🧩 {self.texto}"
