# 🎬 Proyecto CineMaster – Adivina la Película

Aplicación de escritorio desarrollada en **Python + Tkinter + SQLite**, inspirada en el proyecto anterior **MixMaster (simulador de cócteles)**, pero adaptada al ámbito del cine.

CineMaster es un juego en el que el usuario debe **adivinar películas a partir de pistas**, gestionando su propio ranking de puntuaciones y una base de datos con las películas disponibles.

---

## 📚 Información general

- **Nombre del proyecto:** CineMaster – Adivina la Película  
- **Lenguaje:** Python 3  
- **Interfaz:** Tkinter  
- **Base de datos:** SQLite  
- **Duración estimada del desarrollo:** 6 horas  
- **Autor:** David Gutiérrez Ortiz  

---

## 🧩 Estructura del proyecto

```plaintext
Proyecto_AdivinaPeliculaAlt/
│
├── main.py                          # Archivo principal (punto de entrada)
│
├── controller/
│   ├── controller.py                # Controlador principal del juego
│   └── datos_iniciales.py           # Script auxiliar con datos y ranking de ejemplo
│
├── data/
│   ├── gestor_bd.py                 # Conexión y gestión de la base de datos SQLite
│   └── db_cinemaster.db             # Base de datos (se genera automáticamente)
│
├── model/
│   ├── pelicula.py                  # Clase Pelicula
│   └── pista.py                     # Clase Pista
│
├── view/
│   └── interfaz.py                  # Interfaz gráfica con Tkinter
│
└── resources/
    └── img/                         # Carpeta para imágenes (logo, iconos, etc.)

```
---

## 🧠 Descripción técnica

### 🗄️ **GestorBD (`data/gestor_bd.py`)**

- Gestiona la conexión con la base de datos SQLite.  
- Crea las tablas `peliculas`, `pistas` y `puntuaciones`.  
- Permite insertar, leer y eliminar registros.  
- Incluye un pequeño ajuste técnico opcional (`row_factory = sqlite3.Row`)  
  para acceder a los datos por nombre de columna en vez de por índice, mejorando la legibilidad.

---

### 🧩 **Controller (`controller/controller.py`)**

- Es el “cerebro” del programa.  
- Conecta la interfaz con la base de datos.  
- Permite:  
  - Registrar películas.  
  - Obtener pistas de una película.  
  - Guardar puntuaciones.  
  - Consultar el ranking.  
- Incluye un valor por defecto `"Jugador"` para las partidas sin nombre personalizado.

---

### 🎞️ **Interfaz (`view/interfaz.py`)**

- Desarrollada con **Tkinter** y **PIL** (para mostrar el logo).  
- Permite navegar entre las siguientes pantallas:  
  - 🎬 **Menú principal**  
  - 🎮 **Jugar**  
  - 🏆 **Ver ranking**  
  - ➕ **Añadir película**  
- Estilo visual moderno con paleta **morado-azulada**, inspirada en ambientes cinematográficos nocturnos:

| Elemento | Color | Descripción |
|-----------|--------|-------------|
| Fondo principal | `#1E1B2E` | Morado oscuro, elegante |
| Encabezado | `#2B2640` | Contraste suave |
| Botones principales | `#9C6ADE` | Morado pastel brillante |
| Texto claro | `#E8E6FF` | Blanco-lila suave |

---

### 🎬 **Datos de ejemplo (`controller/datos_iniciales.py`)**

Carga automática de películas y puntuaciones de ejemplo **solo si la base de datos está vacía**.

**Películas iniciales:**
- Matrix  
- Titanic  
- Jurassic Park  
- El Señor de los Anillos: La Comunidad del Anillo  
- Forrest Gump  
- Inception  
- Avatar  

**Ranking de ejemplo:**
- 🥇 David – 100 pts  
- Patri – 80 pts  

---

## 🕹️ Funcionamiento

1. Al ejecutar `main.py`, el programa:  
   - Crea la base de datos (si no existe).  
   - Carga las películas y puntuaciones de ejemplo.  
   - Abre la ventana principal de CineMaster.  

2. Desde el menú principal puedes:  
   - 🎮 **Jugar:** elige una película aleatoria y adivínala a partir de pistas.  
   - 🏆 **Ver Ranking:** consulta el ranking guardado.  
   - 🎬 **Añadir Película:** registra tus propias películas con pistas personalizadas.  
   - 🚪 **Salir:** cierra la aplicación.  

3. Cada partida resta puntos al pedir pistas y guarda la puntuación final al acertar la película.

---

## 💾 Base de datos

Tablas principales del sistema:

| Tabla | Campos | Descripción |
|--------|---------|-------------|
| `peliculas` | id, titulo, genero, anio | Información básica de cada película |
| `pistas` | id, pelicula_id, texto | Pistas asociadas a cada película |
| `puntuaciones` | id, jugador, puntos, fecha | Ranking de jugadores |

---

## 🧹 Reinicializar datos

Si ya has ejecutado el juego y deseas volver al estado inicial:

### 🔸 **Opción 1 – Borrar el archivo**

Elimina manualmente el archivo de base de datos:

```bash
/data/db_cinemaster.db

```
---

### 🔸 **Opción 2 – Desde código**

Ejecuta desde consola o dentro del `main.py`:

```python
controller.limpiar_bd()

from controller.datos_iniciales import cargar_datos_iniciales
cargar_datos_iniciales(controller)

```
---

## 💬 Comentarios finales

Este proyecto combina:

- **Lógica de negocio** (controlador y modelo)  
- **Persistencia de datos** (SQLite)  
- **Interfaz gráfica moderna** (Tkinter)  
- **Estructura modular y mantenible**

Es una **evolución directa del proyecto “MixMaster”** (gestor de cócteles),  
demostrando dominio progresivo de:

- Programación orientada a objetos  
- CRUD en SQLite  
- Diseño de interfaz con Tkinter  
- Integración modular de componentes  

---

## 🧑‍💻 Autor

**David Gutiérrez Ortiz**  
2º DAM – Ilerna Sevilla  

Proyecto realizado como práctica para la asignatura:  
**Sistemas de Gestión Empresarial**

---
