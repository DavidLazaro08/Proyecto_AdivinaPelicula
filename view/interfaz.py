# Clase Interfaz
# Interfaz gráfica principal del proyecto CineMaster.

# Basado en el ejercicio anterior "MixMaster" (simulador de cócteles).
# Se mantiene la estructura general de menús y pantallas,
# adaptada ahora al juego de adivinar películas.

import random
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os


class Interfaz:
    """Interfaz principal del juego CineMaster."""

    def __init__(self, controller):
        self.controller = controller
        self.ventana = tk.Tk()
        self.ventana.title("🎬 CineMaster - Adivina la Película")
        self.ventana.geometry("950x600")
        self.ventana.configure(bg="#1E1B2E")  # Fondo principal morado oscuro

        # ENCABEZADO
        encabezado = tk.Frame(self.ventana, bg="#2B2640", height=80)
        encabezado.pack(fill="x")

        # Logo
        ruta_logo = os.path.join("resources", "img", "logo_cinemaster.png")
        if os.path.exists(ruta_logo):
            logo_img = Image.open(ruta_logo)
            logo_img = logo_img.resize((70, 70), Image.LANCZOS)
            self.logo_tk = ImageTk.PhotoImage(logo_img)
            tk.Label(encabezado, image=self.logo_tk, bg="#2B2640").pack(side="left", padx=15, pady=5)
        else:
            tk.Label(encabezado, text="🎥", bg="#2B2640", fg="#9C6ADE", font=("Helvetica", 26)).pack(side="left", padx=20)

        # Título principal
        tk.Label(encabezado, text="CineMaster",
                 font=("Helvetica", 28, "bold"), fg="#9C6ADE", bg="#2B2640").pack(side="left", padx=10)

        # Contenedor principal
        self.area = tk.Frame(self.ventana, bg="#1E1B2E")
        self.area.pack(fill="both", expand=True)

        self.mostrar_menu_principal()

    # MENÚ PRINCIPAL
    def mostrar_menu_principal(self):
        """Pantalla inicial con los botones principales."""
        for widget in self.area.winfo_children():
            widget.destroy()

        tk.Label(self.area, text="🎬 Bienvenido a CineMaster 🎬",
                 font=("Helvetica", 22, "bold"),
                 fg="#E8E6FF", bg="#1E1B2E").pack(pady=40)

        botones = [
            ("🎮 Jugar", self.mostrar_jugar),
            ("🏆 Ver Ranking", self.mostrar_ranking),
            ("🎬 Añadir Película", self.mostrar_agregar_pelicula),
            ("🚪 Salir", self.ventana.quit)
        ]

        for texto, comando in botones:
            tk.Button(self.area, text=texto, command=comando,
                      font=("Helvetica", 14, "bold"),
                      bg="#9C6ADE", fg="#1E1B2E",
                      activebackground="#B896F2",
                      width=25, height=2, relief="flat",
                      cursor="hand2").pack(pady=10)

    # JUEGO
    def mostrar_jugar(self):
        """Pantalla principal del modo de juego."""
        for widget in self.area.winfo_children():
            widget.destroy()

        peliculas = self.controller.gestor.listar_peliculas()
        if not peliculas:
            tk.Label(self.area, text="No hay películas registradas 😢",
                     font=("Helvetica", 14, "bold"),
                     bg="#1E1B2E", fg="#E8E6FF").pack(pady=40)
            tk.Button(self.area, text="Volver al menú", command=self.mostrar_menu_principal,
                      bg="#9C6ADE", fg="#1E1B2E", width=20).pack(pady=10)
            return

        pelicula = random.choice(peliculas)
        pistas = self.controller.gestor.obtener_pistas_pelicula(pelicula["id"])
        indice_pista = 0
        puntos = tk.IntVar(value=30)

        tk.Label(self.area, text="🎬 ¡Adivina la película!",
                 font=("Helvetica", 18, "bold"),
                 bg="#1E1B2E", fg="#9C6ADE").pack(pady=10)

        lbl_puntos = tk.Label(self.area, text=f"Puntos: {puntos.get()}",
                              font=("Helvetica", 12, "bold"),
                              bg="#1E1B2E", fg="#E8E6FF")
        lbl_puntos.pack()

        lbl_pista = tk.Label(self.area, text="Pulsa 'Mostrar pista' para empezar 🎞️",
                             font=("Helvetica", 11),
                             bg="#1E1B2E", fg="#D4CCF8",
                             wraplength=600, justify="center")
        lbl_pista.pack(pady=15)

        entry_respuesta = tk.Entry(self.area, font=("Helvetica", 12), width=40)
        entry_respuesta.pack(pady=5)

        resultado = tk.Label(self.area, text="", bg="#1E1B2E", fg="#B896F2", font=("Helvetica", 11))
        resultado.pack(pady=5)

        def mostrar_pista():
            nonlocal indice_pista
            if indice_pista < len(pistas):
                lbl_pista.config(text=pistas[indice_pista])
                indice_pista += 1
                puntos.set(puntos.get() - 5)
                lbl_puntos.config(text=f"Puntos: {puntos.get()}")
            else:
                lbl_pista.config(text="❌ No hay más pistas disponibles.")

        def comprobar_respuesta():
            respuesta = entry_respuesta.get().strip().lower()
            if respuesta == pelicula["titulo"].lower():
                resultado.config(text=f"🎉 ¡Correcto! Era {pelicula['titulo']}")
                self.controller.gestor.guardar_puntuacion("Jugador", puntos.get(),
                                                          datetime.now().strftime("%Y-%m-%d %H:%M"))
                messagebox.showinfo("¡Ganaste!", f"Has acertado '{pelicula['titulo']}' con {puntos.get()} puntos.")
                self.mostrar_menu_principal()
            else:
                resultado.config(text="❌ No es correcto, sigue intentándolo...")

        tk.Button(self.area, text="Mostrar pista (-5 pts)", command=mostrar_pista,
                  bg="#9C6ADE", fg="#1E1B2E", width=20).pack(pady=5)
        tk.Button(self.area, text="Comprobar", command=comprobar_respuesta,
                  bg="#9C6ADE", fg="#1E1B2E", width=20).pack(pady=5)
        tk.Button(self.area, text="Volver al menú", command=self.mostrar_menu_principal,
                  bg="#514A72", fg="#E8E6FF", width=20).pack(pady=10)

    # RANKING
    def mostrar_ranking(self):
        """Pantalla con el ranking de jugadores."""
        for widget in self.area.winfo_children():
            widget.destroy()

        tk.Label(self.area, text="🏆 Ranking de jugadores",
                 font=("Helvetica", 18, "bold"),
                 fg="#9C6ADE", bg="#1E1B2E").pack(pady=20)

        ranking = self.controller.obtener_ranking()
        if not ranking:
            tk.Label(self.area, text="Aún no hay puntuaciones registradas.",
                     font=("Helvetica", 12),
                     fg="#CCCCCC", bg="#1E1B2E").pack(pady=20)
        else:
            tabla = ttk.Treeview(self.area, columns=("Jugador", "Puntos", "Fecha"), show="headings", height=10)
            tabla.heading("Jugador", text="Jugador")
            tabla.heading("Puntos", text="Puntos")
            tabla.heading("Fecha", text="Fecha")

            for fila in ranking:
                tabla.insert("", "end", values=(fila["jugador"], fila["puntos"], fila["fecha"]))
            tabla.pack(pady=10)

        tk.Button(self.area, text="⬅ Volver al menú", command=self.mostrar_menu_principal,
                  bg="#9C6ADE", fg="#1E1B2E",
                  font=("Helvetica", 12, "bold"), width=20).pack(pady=20)

    # AGREGAR PELÍCULA
    def mostrar_agregar_pelicula(self):
        """Pantalla para registrar nuevas películas."""
        for widget in self.area.winfo_children():
            widget.destroy()

        tk.Label(self.area, text="🎬 Agregar nueva película",
                 font=("Helvetica", 18, "bold"),
                 fg="#9C6ADE", bg="#1E1B2E").pack(pady=10)

        frame = tk.Frame(self.area, bg="#1E1B2E")
        frame.pack(pady=20)

        campos = [("Título", ""), ("Género", ""), ("Año", ""), ("Pistas (una por línea)", "multilinea")]
        entradas = {}

        for i, (label, tipo) in enumerate(campos):
            tk.Label(frame, text=label + ":", bg="#1E1B2E", fg="#E8E6FF").grid(row=i, column=0, padx=10, pady=5, sticky="e")

            if tipo == "multilinea":
                txt = tk.Text(frame, width=40, height=5)
                txt.grid(row=i, column=1, padx=10, pady=5)
                entradas[label] = txt
            else:
                ent = tk.Entry(frame, width=40)
                ent.grid(row=i, column=1, padx=10, pady=5)
                entradas[label] = ent

        def guardar_pelicula():
            titulo = entradas["Título"].get().strip()
            genero = entradas["Género"].get().strip()
            anio = entradas["Año"].get().strip()
            pistas_texto = entradas["Pistas (una por línea)"].get("1.0", tk.END).strip().splitlines()

            if not titulo or not pistas_texto:
                messagebox.showerror("Error", "Debes rellenar el título y al menos una pista.")
                return

            try:
                anio = int(anio) if anio else None
            except ValueError:
                messagebox.showerror("Error", "El año debe ser un número.")
                return

            self.controller.registrar_pelicula(titulo, genero, anio, pistas_texto)
            messagebox.showinfo("Éxito", f"Película '{titulo}' agregada correctamente.")
            self.mostrar_menu_principal()

        tk.Button(self.area, text="💾 Guardar", command=guardar_pelicula,
                  bg="#9C6ADE", fg="#1E1B2E",
                  font=("Helvetica", 12, "bold"), width=20).pack(pady=10)
        tk.Button(self.area, text="⬅ Volver", command=self.mostrar_menu_principal,
                  bg="#514A72", fg="#E8E6FF",
                  font=("Helvetica", 12), width=20).pack(pady=10)

    # LOOP
    def iniciar(self):
        """Inicia el bucle principal de la ventana."""
        self.ventana.mainloop()
