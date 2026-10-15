import tkinter as tk
from tkinter import messagebox, ttk
from persistencia import cargar_datos, guardar_datos

# Importamos las funciones de gestión que ya creamos y probamos en consola
from gestion import (
    actualizar_datos_mascota,
    actualizar_tarifa_por_servicio,
    consultar_citas_de_mascota,
    consultar_mascota_por_id,
    consultar_servicio_por_id,
    ejecutar_cancelacion_cita,
    ejecutar_eliminacion_mascota,
    mostrar_citas_activas,
    mostrar_mascotas,
    mostrar_todas_las_citas,
    mostrar_todos_los_servicios,
    registrar_cita,
    registrar_mascota,
    validacion_cancelar_cita,
    validar_se_puede_eliminar_mascota,
    buscar_mascotas_de_cliente,
    buscar_mascota_por_id,
    consultar_citas_por_id,
    mostrar_clientes,
    consultar_cliente_por_id,
    registrar_cliente,
    actualizar_telefono_cliente,
    validar_se_puede_eliminar_cliente,
    ejecutar_eliminacion_cliente
)


class InterfazChikPets:
    """Interfaz gráfica principal de Chik & Pets."""

    def __init__(self, clientes, mascotas, servicios, citas):
        self.clientes = clientes
        self.mascotas = mascotas
        self.servicios = servicios
        self.citas = citas

        self.ventana = tk.Tk()
        self.ventana.title("Chik & Pets - Sistema de Gestión Profesional")
        self.ventana.geometry("980x650")
        self.ventana.minsize(900, 580)

        self.crear_encabezado()
        self.crear_pestanas()
        self.crear_barra_inferior()

        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

    def guardar_cambios(self):
        guardar_datos(self.clientes, self.mascotas, self.servicios, self.citas)

    def crear_encabezado(self):
        titulo = ttk.Label(
            self.ventana,
            text="🐾 Chik & Pets - Sistema de Gestión Veterinaria",
            font=("Tahoma", 16, "bold"),
        )
        titulo.pack(pady=(12, 4))

        subtitulo = ttk.Label(
            self.ventana,
            text=(
                "Gestión integral de mascotas, servicios, citas y control de"
                " atención"
            ),
            font=("Tahoma", 10),
        )
        subtitulo.pack(pady=(0, 8))

    def crear_pestanas(self):
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(fill="both", expand=True, padx=12, pady=8)

        self.tab_mascotas = ttk.Frame(self.notebook)
        self.tab_servicios = ttk.Frame(self.notebook)
        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_citas = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_mascotas, text="🐶 Mascotas")
        self.notebook.add(self.tab_servicios, text="✂️ Servicios")
        self.notebook.add(self.tab_clientes, text="Clientes")
        self.notebook.add(self.tab_citas, text="📅 Citas")

        self.crear_tab_mascotas()
        self.crear_tab_servicios()
        self.crear_tab_clientes()
        self.crear_tab_citas()
        

    def crear_barra_inferior(self):
        marco = ttk.Frame(self.ventana)
        marco.pack(fill="x", padx=12, pady=(0, 12))

        ttk.Button(marco, text="Salir", command=self.cerrar_aplicacion).pack(
            side="right"
        )

        self.etiqueta_estado = ttk.Label(
            marco, text="Sistema listo para operar.", font=("Tahoma", 10)
        )
        self.etiqueta_estado.pack(side="left")

    # --------------------------------------------------------
    #  MÉTODOS MAESTROS REUTILIZABLES (MODULARIZACIÓN)
    # --------------------------------------------------------
    # Muestra lo retornado por la funcion de gestion y permite cerrar la ventana flotante 
    def mostrar_resultado(self, exito, mensaje, ventana_toplevel=None):
        """Maneja centralizadamente los mensajes y estados."""
        self.etiqueta_estado.config(text=str(mensaje))
        if exito:
            messagebox.showinfo("Chik & Pets", str(mensaje))
            if ventana_toplevel:
                ventana_toplevel.destroy()
        else:
            messagebox.showwarning("Chik & Pets", str(mensaje))

    def abrir_ventana_input_unico(
        self, titulo_ventana, texto_label, comando_boton
    ):
        """Método genérico para abrir cualquier ventana emergente de un solo campo (ID)."""
        ventana = tk.Toplevel(self.ventana)
        ventana.title(titulo_ventana)
        ventana.geometry("400x260")
        ventana.grab_set()

        tk.Label(
            ventana, text=titulo_ventana, font=("Tahoma", 14, "bold")
        ).pack(pady=12)

        form = ttk.Frame(ventana)
        form.pack(padx=20, pady=5, fill="both", expand=True)

        ttk.Label(form, text=texto_label).grid(
            row=0, column=0, sticky="w", pady=10
        )
        entrada = ttk.Entry(form, width=22)
        entrada.grid(row=0, column=1, sticky="w")

        ttk.Button(ventana, text="Ejecutar", command=comando_boton).pack(pady=15)
        return ventana, entrada #La ventana flotante y el ID que escribio el usuario

#Limpiar texto principal y mostrar resuktado en este.
    def imprimir_en_pantalla_principal(self, widget_texto, titulo_seccion, contenido):
        """Método genérico para volcar resultados en la caja de texto principal."""
        widget_texto.config(state="normal")
        widget_texto.delete("1.0", tk.END)
        widget_texto.insert(
            tk.END, f"{titulo_seccion}\n" + "=" * 30 + "\n"
        )

        if isinstance(contenido, list):
            for item in contenido:
                widget_texto.insert(tk.END, str(item) + "\n")
        else:
            widget_texto.insert(tk.END, str(contenido) + "\n")

        widget_texto.config(state="disabled")

    # --------------------------------------------------------
    # PESTAÑA MASCOTAS
    # --------------------------------------------------------
    def crear_tab_mascotas(self):
        panel_botones = ttk.LabelFrame(
            self.tab_mascotas, text="Acciones de Gestión de Mascotas"
        )
        panel_botones.pack(fill="x", padx=15, pady=15)

        fila_1 = ttk.Frame(panel_botones)
        fila_1.pack(pady=5)
        fila_2 = ttk.Frame(panel_botones)
        fila_2.pack(pady=5)

        ttk.Button(
            fila_1,
            text="➕ Registrar Mascota",
            command=self.abrir_ventana_registrar_mascota,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_1,
            text="🔍 Consultar por ID",
            command=self.abrir_ventana_buscar_mascotas_gui,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_1,
            text="🔄 Mostrar información mascotas",
            command=self.mostrar_mascotas_gui,
        ).pack(side="left", padx=8, pady=8)

        ttk.Button(
            fila_2,
            text="Buscar mascota por cliente",
            command=self.abrir_ventana_mascota_cliente,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_2,
            text="Consultar citas de mascota",
            command=self.abrir_ventana_buscar_citas_mascota,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_2,
            text="Eliminar mascota",
            command=self.abrir_ventana_eliminar_mascota,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_2,
            text="Actualizar datos mascota",
            command=self.abrir_ventana_actualizar_mascota,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_2,
            text="🧹 Limpiar Pantalla",
            command=self.limpiar_pantalla_mascotas,
        ).pack(side="left", padx=8, pady=8)

        panel_texto = ttk.LabelFrame(
            self.tab_mascotas, text="Información de Mascotas Registradas"
        )
        panel_texto.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.texto_mascotas = tk.Text(
            panel_texto, height=12, width=70, font=("Tahoma", 10), state="disabled"
        )
        self.texto_mascotas.pack(padx=10, pady=10, fill="both", expand=True)

    def limpiar_pantalla_mascotas(self):
        self.texto_mascotas.config(state="normal")
        self.texto_mascotas.delete("1.0", tk.END)
        self.texto_mascotas.config(state="disabled")
        self.etiqueta_estado.config(text="Pantalla limpiada.")

    def mostrar_mascotas_gui(self):
        #Función de gestion
        exito, datos = mostrar_mascotas(self.mascotas)
        if exito:
            self.imprimir_en_pantalla_principal(self.texto_mascotas,
                "LISTA GENERAL DE MASCOTAS", datos
            )
            self.etiqueta_estado.config(text="Lista de mascotas cargada con éxito.")
        else:
            self.imprimir_en_pantalla_principal(self.texto_mascotas,"AVISO", datos)
            self.etiqueta_estado.config(text=str(datos))

    # --------------------------------------------------------
    # ACCIONES Y VENTANAS USANDO LOS MÉTODOS REUTILIZABLES
    # --------------------------------------------------------
    def abrir_ventana_registrar_mascota(self):
        self.ventana_reg_mascota = tk.Toplevel(self.ventana)
        self.ventana_reg_mascota.title("Registrar Nueva Mascota")
        self.ventana_reg_mascota.geometry("400x350")
        self.ventana_reg_mascota.grab_set()

        tk.Label(
            self.ventana_reg_mascota,
            text="🐾 Formulario de Registro",
            font=("Tahoma", 13, "bold"),
        ).pack(pady=12)
        form = ttk.Frame(self.ventana_reg_mascota)
        form.pack(padx=20, pady=5, fill="both", expand=True)

        ttk.Label(form, text="ID del Dueño:").grid(
            row=0, column=0, sticky="w", pady=8
        )
        self.input_dueño = ttk.Entry(form, width=25)
        self.input_dueño.grid(row=0, column=1, pady=8, padx=5)

        ttk.Label(form, text="Nombre:").grid(row=1, column=0, sticky="w", pady=8)
        self.input_nombre_mascota = ttk.Entry(form, width=25)
        self.input_nombre_mascota.grid(row=1, column=1, pady=8, padx=5)

        ttk.Label(form, text="Especie:").grid(row=2, column=0, sticky="w", pady=8)
        self.combo_especie = ttk.Combobox(
            form, values=["perro", "gato", "conejo"], state="readonly", width=23
        )
        self.combo_especie.grid(row=2, column=1, pady=8, padx=5)
        self.combo_especie.set("perro")
        self.combo_especie.bind("<<ComboboxSelected>>", self.actualizar_razas_combo)

        ttk.Label(form, text="Raza:").grid(row=3, column=0, sticky="w", pady=8)
        self.combo_raza = ttk.Combobox(form, state="readonly", width=23)
        self.combo_raza.grid(row=3, column=1, pady=8, padx=5)
        self.actualizar_razas_combo()

        ttk.Button(
            self.ventana_reg_mascota,
            text="Guardar Registro",
            command=self.ejecutar_registro_mascota_gui,
        ).pack(pady=20)

    def actualizar_razas_combo(self, evento=None):
        especies_y_razas = {
            "perro": [
                "criollo",
                "bulldog",
                "chihuahua",
                "pug",
                "golden",
                "pastor alemán",
                "french poodle",
            ],
            "gato": ["criollo", "persa", "siamés", "maine coon", "ragdoll", "bengalí"],
            "conejo": ["enano holandés", "cabeza de león", "mini rex", "mini lop", "holland lop"]
        }
        esp = self.combo_especie.get()
        razas = especies_y_razas.get(esp, [])
        self.combo_raza["values"] = razas
        if razas:
            self.combo_raza.set(razas[0])

    def ejecutar_registro_mascota_gui(self):
        nombre = self.input_nombre_mascota.get().strip()
        id_dueno = self.input_dueño.get().strip()
        if not nombre or not id_dueno:
            messagebox.showwarning("campos vacios","Los campos no pueden estar vacios")
            return
        exito, mensaje = registrar_mascota(
            self.mascotas,
            self.clientes,
            self.input_nombre_mascota.get().strip(),
            self.combo_especie.get().strip(),
            self.combo_raza.get().strip(),
            self.input_dueño.get().strip().upper(),
        )
        
        if exito:
            self.guardar_cambios()
        self.mostrar_resultado(exito, mensaje, self.ventana_reg_mascota)
        if exito:
            self.mostrar_mascotas_gui()

    #  Buscar por ID
    def abrir_ventana_buscar_mascotas_gui(self):
        self.ventana_busq, self.input_id_consulta = self.abrir_ventana_input_unico(
            "Buscar por ID", "ID de la Mascota:", self.ejecutar_consulta_mascota_gui
        )

    def ejecutar_consulta_mascota_gui(self):
        id_mascota = self.input_id_consulta.get().strip().upper()
        if not id_mascota:
            messagebox.showwarning("Vacío", "Ingrese un ID.")
            return
        exito, res = consultar_mascota_por_id(self.mascotas, id_mascota)
        if exito:
            self.imprimir_en_pantalla_principal(self.texto_mascotas,"RESULTADO DE BÚSQUEDA", res)
            self.mostrar_resultado(True, "Mascota consultada con éxito", self.ventana_busq)
        else:
            self.mostrar_resultado(False, res)

    # Buscar por Cliente
    def abrir_ventana_mascota_cliente(self):
        self.ventana_cli, self.input_id_cliente = self.abrir_ventana_input_unico(
            "Buscar por Cliente", "ID del Cliente:", self.ejecutar_busqueda_mascota_cliente_gui
        )

    def ejecutar_busqueda_mascota_cliente_gui(self):
        id_c = self.input_id_cliente.get().strip().upper()
        if not id_c:
            messagebox.showwarning("Vacío", "Ingrese un ID de cliente.")
            return
        exito, msg = buscar_mascotas_de_cliente(self.mascotas, id_c, self.clientes)
        if exito:
            self.imprimir_en_pantalla_principal(self.texto_mascotas,"MASCOTAS DEL CLIENTE", msg)
            self.mostrar_resultado(True, "Consulta exitosa", self.ventana_cli)
        else:
            self.mostrar_resultado(False, msg)

    #  Buscar Citas de Mascota
    def abrir_ventana_buscar_citas_mascota(self):
        self.ventana_cit, self.input_id_mascota_cita = self.abrir_ventana_input_unico(
            "Citas de Mascota", "ID de la Mascota:", self.ejecutar_busqueda_de_citas_mascota_gui
        )

    def ejecutar_busqueda_de_citas_mascota_gui(self):
        id_m = self.input_id_mascota_cita.get().strip().upper()
        if not id_m:
            messagebox.showwarning("Vacío", "Ingrese un ID.")
            return
        exito, msg = consultar_citas_de_mascota(self.citas, self.mascotas, id_m)
        if exito:
            self.imprimir_en_pantalla_principal(self.texto_mascotas,"CITAS ENCONTRADAS", msg)
            self.mostrar_resultado(True, "Citas consultadas", self.ventana_cit)
        else:
            self.mostrar_resultado(False, msg)

    # Eliminar Mascota
    def abrir_ventana_eliminar_mascota(self):
        self.ventana_elim, self.input_id_mascota_eliminar = self.abrir_ventana_input_unico(
            "Eliminar Mascota", "ID de la Mascota:", self.ejecutar_eliminacion_de_mascota_gui
        )

    def ejecutar_eliminacion_de_mascota_gui(self):
        id_m = self.input_id_mascota_eliminar.get().strip().upper()
        if not id_m:
            messagebox.showwarning("Vacío", "Ingrese un ID.")
            return
        exito, msg = validar_se_puede_eliminar_mascota(self.mascotas, id_m, self.citas)
        if exito:
            if messagebox.askyesno("Confirmar", f"¿Eliminar a {id_m}?"):
                ex_del, msg_del = ejecutar_eliminacion_mascota(self.mascotas, id_m)
                if ex_del:
                    self.guardar_cambios()
                self.mostrar_resultado(ex_del, msg_del, self.ventana_elim)
                self.mostrar_mascotas_gui()
            else:
                messagebox.showinfo("Eliminacion","No se realizo la eliminación")
        else:
            self.mostrar_resultado(False, msg)

    # ACTUALIZAR DATOS MASCOTA
    def abrir_ventana_actualizar_mascota(self):
        self.ventana_actualizar = tk.Toplevel(self.ventana)
        self.ventana_actualizar.title("Actualizar Mascota")
        self.ventana_actualizar.geometry("420x320")
        self.ventana_actualizar.grab_set()

        tk.Label(
            self.ventana_actualizar,
            text="✏️ Actualizar Datos",
            font=("Tahoma", 13, "bold"),
        ).pack(pady=12)
        form = ttk.Frame(self.ventana_actualizar)
        form.pack(padx=20, pady=5, fill="both", expand=True)

        ttk.Label(form, text="ID de la Mascota:").grid(row=0, column=0, sticky="w", pady=8)
        self.input_id_mascota_act = ttk.Entry(form, width=25)
        self.input_id_mascota_act.grid(row=0, column=1, sticky="w", pady=8)

        ttk.Label(form, text="Nueva Especie:").grid(row=1, column=0, sticky="w", pady=8)
        self.combo_especie_act = ttk.Combobox(
            form, values=["perro", "gato", "conejo"], state="readonly", width=23
        )
        self.combo_especie_act.grid(row=1, column=1, pady=8, padx=5)
        self.combo_especie_act.set("perro")
        self.combo_especie_act.bind("<<ComboboxSelected>>", self.actualizar_razas_combo_act)

        ttk.Label(form, text="Nueva Raza:").grid(row=2, column=0, sticky="w", pady=8)
        self.combo_raza_act = ttk.Combobox(form, state="readonly", width=23)
        self.combo_raza_act.grid(row=2, column=1, pady=8, padx=5)
        self.actualizar_razas_combo_act()

        ttk.Button(
            self.ventana_actualizar,
            text="Actualizar",
            command=self.ejecutar_actualizacion_mascota_gui,
        ).pack(pady=20)

    def actualizar_razas_combo_act(self, evento=None):
        esp = self.combo_especie_act.get()
        razas = {
            "perro": ["criollo", "bulldog", "chihuahua", "pug", "golden", "pastor alemán", "french poodle"],
            "gato": ["criollo", "persa", "siamés", "maine coon", "ragdoll", "bengalí"],
            "conejo": ["enano holandés", "cabeza de león", "mini rex", "mini lop", "holland lop"]
        }.get(esp, [])
        self.combo_raza_act["values"] = razas
        if razas:
            self.combo_raza_act.set(razas[0])

    def ejecutar_actualizacion_mascota_gui(self):
        id_m = self.input_id_mascota_act.get().strip().upper()
        if not id_m:
            messagebox.showwarning("Vacío", "Ingrese un ID.")
            return
        exito, msg = actualizar_datos_mascota(
            self.mascotas, id_m, self.combo_especie_act.get(), self.combo_raza_act.get()
        )
        if exito:
            self.guardar_cambios()
            mascota = buscar_mascota_por_id(self.mascotas, id_m)
            if mascota:
                self.imprimir_en_pantalla_principal(self.texto_mascotas,"MASCOTA ACTUALIZADA", [mascota.obtener_informacion()])
            self.mostrar_resultado(True, msg, self.ventana_actualizar)
            self.mostrar_mascotas_gui()
        else:
            self.mostrar_resultado(False, msg)

    def crear_tab_servicios(self):
        panel = ttk.LabelFrame(self.tab_servicios, text="Gestión de Servicios")
        panel.pack(fill="x", padx=15, pady=15)
        ttk.Button(panel, text="Mostrar servicios", command=self.mostrar_servicios_gui).pack(side="left", padx=8, pady=10)
        ttk.Button(panel, text="Buscar servicio por ID", command=self.buscar_servicio_gui).pack(side="left", padx=8, pady=10)
        ttk.Button(panel, text="Actualizar tarifa", command=self.actualizar_tarifa_gui).pack(side="left", padx=8, pady=10)
        self.texto_servicios = tk.Text(self.tab_servicios, height=12, state="disabled")
        self.texto_servicios.pack(fill="both", expand=True, padx=15, pady=10)

    def mostrar_servicios_gui(self):
        exito, datos = mostrar_todos_los_servicios(self.servicios)
        self.imprimir_en_pantalla_principal(self.texto_servicios, "SERVICIOS", datos)

    def buscar_servicio_gui(self):
        self.ventana_servicio, self.input_servicio_buscar = self.abrir_ventana_input_unico(
            "Buscar servicio", "ID del servicio:", self.ejecutar_buscar_servicio_gui
        )

    def ejecutar_buscar_servicio_gui(self):
        id_servicio = self.input_servicio_buscar.get().strip().upper()
        exito, datos = consultar_servicio_por_id(self.servicios, id_servicio)
        if exito:
            self.imprimir_en_pantalla_principal(self.texto_servicios, "SERVICIO", datos)
        self.mostrar_resultado(exito, datos if not exito else "Servicio encontrado", self.ventana_servicio)

    def actualizar_tarifa_gui(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Actualizar tarifa de servicio")
        ventana.geometry("400x200")
        ventana.grab_set()
        ttk.Label(ventana, text="ID del servicio:").pack(pady=3)
        entrada_id = ttk.Entry(ventana)
        entrada_id.pack()
        ttk.Label(ventana, text="Nueva tarifa (número entero):").pack(pady=3)
        entrada_tarifa = ttk.Entry(ventana)
        entrada_tarifa.pack()

        def confirmar():
            try:
                nueva_tarifa = int(entrada_tarifa.get().strip())
            except ValueError:
                self.mostrar_resultado(False, "Ingrese una tarifa numérica válida.")
                return
            exito, datos = actualizar_tarifa_por_servicio(
                self.servicios, nueva_tarifa, entrada_id.get().strip().upper()
            )
            if exito:
                self.guardar_cambios()
                self.mostrar_servicios_gui()
            self.mostrar_resultado(exito, datos, ventana)

        ttk.Button(ventana, text="Actualizar", command=confirmar).pack(pady=10)
    def crear_tab_clientes(self):
        
        panel_botones = ttk.LabelFrame(
                        self.tab_clientes,text="Acciones de Gestión de Clientes"
                    )
        panel_botones.pack(fill="x", padx=15, pady=15)
    
        fila_1 = ttk.Frame(panel_botones)
        fila_1.pack(pady=5)
        fila_2 = ttk.Frame(panel_botones)
        fila_2.pack(pady=5)
    
        ttk.Button(
            fila_1,
            text="➕ Registrar cliente",
            command=self.registrar_cliente_gui,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_1,
            text="🔍 Consultar cliente por ID",
            command=self.consultar_cliente_por_id,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_1,
            text="🔄 Mostrar información clientes",
            command=self.mostrar_clientes_gui,
        ).pack(side="left", padx=8, pady=8)

        ttk.Button(
            fila_2,
            text="Consultar mascotas de clientes",
            command=self.consultar_mascotas_de_cliente_gui,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_2,
            text="Actualizar telefono de cliente",
            command=self.actualizar_telefono_gui,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_2,
            text="Eliminar cliente",
            command=self.eliminar_cliente_gui,
        ).pack(side="left", padx=10, pady=10)
        
        ttk.Button(
            fila_2,
            text="🧹 Limpiar Pantalla",
            command=self.limpiar_pantalla_clientes,
        ).pack(side="left", padx=8, pady=8)

        panel_texto = ttk.LabelFrame(
            self.tab_clientes, text="Información de Clientes Registrados"
        )
        panel_texto.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.texto_clientes = tk.Text(
            panel_texto, height=12, width=70, font=("Tahoma", 10), state="disabled"
        )
        self.texto_clientes.pack(padx=10, pady=10, fill="both", expand=True)
        
    def limpiar_pantalla_clientes(self):
        self.texto_clientes.config(state="normal")
        self.texto_clientes.delete("1.0", tk.END)
        self.texto_clientes.config(state="disabled")
        self.etiqueta_estado.config(text="Pantalla limpiada.")
                    
        
    def registrar_cliente_gui(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registrar cliente")
        ventana.geometry("400x230")
        ventana.grab_set()
        ttk.Label(ventana, text="ID del cliente:").pack()
        entrada_id = ttk.Entry(ventana)
        entrada_id.pack()
        ttk.Label(ventana, text="Nombre del cliente:").pack()
        entrada_nombre = ttk.Entry(ventana)
        entrada_nombre.pack()
        ttk.Label(ventana, text="Teléfono (10 dígitos):").pack()
        entrada_telefono = ttk.Entry(ventana)
        entrada_telefono.pack()

        def confirmar():
            exito, mensaje = registrar_cliente(
                self.clientes, entrada_id.get().strip().upper(),
                entrada_nombre.get().strip(), entrada_telefono.get().strip()
            )
            if exito:
                self.guardar_cambios()
                self.mostrar_clientes_gui()
            self.mostrar_resultado(exito, mensaje, ventana)

        ttk.Button(ventana, text="Registrar", command=confirmar).pack(pady=10)

    def consultar_mascotas_de_cliente_gui(self):
        ventana, entrada = self.abrir_ventana_input_unico(
            "Mascotas del cliente", "ID del cliente:", lambda: consultar()
        )

        def consultar():
            exito, datos = buscar_mascotas_de_cliente(
                self.mascotas, entrada.get().strip().upper(), self.clientes
            )
            if exito:
                self.imprimir_en_pantalla_principal(self.texto_clientes, "MASCOTAS DEL CLIENTE", datos)
            self.mostrar_resultado(exito, "Consulta realizada" if exito else datos, ventana)

    def actualizar_telefono_gui(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Actualizar teléfono")
        ventana.geometry("400x190")
        ventana.grab_set()
        ttk.Label(ventana, text="ID del cliente:").pack()
        entrada_id = ttk.Entry(ventana)
        entrada_id.pack()
        ttk.Label(ventana, text="Nuevo teléfono (10 dígitos):").pack()
        entrada_tel = ttk.Entry(ventana)
        entrada_tel.pack()

        def confirmar():
            exito, mensaje = actualizar_telefono_cliente(
                self.clientes, entrada_id.get().strip().upper(), entrada_tel.get().strip()
            )
            if exito:
                self.guardar_cambios()
                self.mostrar_clientes_gui()
            self.mostrar_resultado(exito, mensaje, ventana)

        ttk.Button(ventana, text="Actualizar", command=confirmar).pack(pady=10)

    def eliminar_cliente_gui(self):
        ventana, entrada = self.abrir_ventana_input_unico(
            "Eliminar cliente", "ID del cliente:", lambda: confirmar()
        )

        def confirmar():
            id_cliente = entrada.get().strip().upper()
            exito, mensaje = validar_se_puede_eliminar_cliente(
                self.clientes, id_cliente, self.mascotas
            )
            if not exito:
                self.mostrar_resultado(False, mensaje)
                return
            if messagebox.askyesno("Confirmar", "¿Desea eliminar este cliente?"):
                exito, mensaje = ejecutar_eliminacion_cliente(self.clientes, id_cliente)
                if exito:
                    self.guardar_cambios()
                    self.mostrar_clientes_gui()
                self.mostrar_resultado(exito, mensaje, ventana)

    def mostrar_clientes_gui (self):
        
        exito,datos = mostrar_clientes(self.clientes)
        
        if exito:
            self.imprimir_en_pantalla_principal(self.texto_clientes,"INFORMACIÓN CLIENTES",datos)
            self.etiqueta_estado.config(text="Información clientes")
        else:
            self.imprimir_en_pantalla_principal(self.texto_clientes,"AVISO",datos)
            
    def consultar_cliente_por_id(self):
        
        self.ventana_cliente_id, self.input_id_cliente = self.abrir_ventana_input_unico("Buscar cliente por ID","ID cliente:",self.consultar_cliente_id_gui) 
        
    def consultar_cliente_id_gui(self):

        id_cliente = self.input_id_cliente.get().upper().strip()
        if not id_cliente:
            messagebox.showwarning("Campo vacío","El campo no puede estar vacío")
            return
        exito,datos = consultar_cliente_por_id(self.clientes,id_cliente)
        if exito:
            self.imprimir_en_pantalla_principal(self.texto_clientes,"Cliente por ID",datos)
            self.mostrar_resultado(True,"Se consulto correctamente",self.ventana_cliente_id)
            self.etiqueta_estado.config(text="Cliente por ID")
        else:
            self.imprimir_en_pantalla_principal(self.texto_clientes,"AVISO",datos)
            self.mostrar_resultado(False,datos,self.ventana_cliente_id)
        

   
    def crear_tab_citas(self):
        
        panel = ttk.LabelFrame(self.tab_citas, text="Gestión de Citas")
        panel.pack(fill="both", expand=True, padx=15, pady=15)
        panel_botones = ttk.LabelFrame(
                    self.tab_citas, text="Acciones de Gestión de Citas"
                )
        panel_botones.pack(fill="x", padx=15, pady=15)

        fila_1 = ttk.Frame(panel_botones)
        fila_1.pack(pady=5)
        fila_2 = ttk.Frame(panel_botones)
        fila_2.pack(pady=5)

        ttk.Button(
            fila_1,
            text="➕ Registrar Cita",
            command=self.registrar_cita,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_1,
            text="🔍 Consultar cita por ID",
            command=self.buscar_citas_por_id,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_1,
            text="🔄 Mostrar información citas",
            command=self.mostrar_citas_gui,
        ).pack(side="left", padx=8, pady=8)

        ttk.Button(
            fila_2,
            text="Consultar citas de mascota",
            command=self.consultar_citas_mascota,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_2,
            text="Consultar citas activas",
            command=self.buscar_citas_activas,
        ).pack(side="left", padx=10, pady=10)
        ttk.Button(
            fila_2,
            text="Cancelar cita",
            command=self.cancelar_cita,
        ).pack(side="left", padx=10, pady=10)
        
        ttk.Button(
            fila_2,
            text="🧹 Limpiar Pantalla",
            command=self.limpiar_pantalla_citas,
        ).pack(side="left", padx=8, pady=8)

        panel_texto = ttk.LabelFrame(
            self.tab_citas, text="Información de Citas Registradas"
        )
        panel_texto.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.texto_citas = tk.Text(
            panel_texto, height=12, width=70, font=("Tahoma", 10), state="disabled"
        )
        self.texto_citas.pack(padx=10, pady=10, fill="both", expand=True)
        
    def limpiar_pantalla_citas(self):
        self.texto_citas.config(state="normal")
        self.texto_citas.delete("1.0", tk.END)
        self.texto_citas.config(state="disabled")
        self.etiqueta_estado.config(text="Pantalla limpiada.")
        
    #MOSTRAR CITAS
    def mostrar_citas_gui(self):
        
        exito,datos = mostrar_todas_las_citas(self.citas)

        if exito:
            self.imprimir_en_pantalla_principal(self.texto_citas,"INFORMACIÓN CITAS",datos)
            self.etiqueta_estado.config(text="Información citas")
        else:
            self.imprimir_en_pantalla_principal(self.texto_citas,"AVISO",datos)
            self.etiqueta_estado.config(text="No se logro mostrar información de citas.")
    
    def buscar_citas_por_id(self):
        
        self.ventana_id_cita,self.input_id_cita = self.abrir_ventana_input_unico("Cita por ID","ID cita:",self.buscar_cita_por_id_gui)
    
    def buscar_cita_por_id_gui(self):
        
        self.id_cita = self.input_id_cita.get().strip().upper()
        
        if not self.id_cita:
            messagebox.showwarning("Campo vacio","Este campo no puede estar vacio.")
            return
        
        exito,dato = consultar_citas_por_id(self.citas,self.id_cita)
        
        if exito:
            self.imprimir_en_pantalla_principal(self.texto_citas,"CITA POR ID",dato)
            self.mostrar_resultado(True,"Cita consultada con exito",self.ventana_id_cita)
        else:
            self.mostrar_resultado(False,dato)
            
    
    def buscar_citas_activas(self):
        
        exito,datos = mostrar_citas_activas(self.citas)
        
        if exito:
            self.imprimir_en_pantalla_principal(self.texto_citas,"CITAS ACTIVAS",datos)
            self.etiqueta_estado.config(text="Citas activas")
        else:
            self.imprimir_en_pantalla_principal(self.texto_citas,"AVISO",datos)
            self.etiqueta_estado.config(text="No hay citas activas")
            
    def consultar_citas_mascota(self):        
        
        self.ventana_cita_mascota,self.input_id_mascota = self.abrir_ventana_input_unico("Buscar citas de mascota","ID mascota:",self.ejecutar_citas_mascota)
    
    def ejecutar_citas_mascota(self):
        
        id_mascota = self.input_id_mascota.get().upper()
        
        if not id_mascota:
            messagebox.showwarning("Campo vacio","Este campo no puede estar vacío")
            return
        
        exito,datos = consultar_citas_de_mascota(self.citas,self.mascotas,id_mascota)
        
        if exito:
            
            self.imprimir_en_pantalla_principal(self.texto_citas,"CITAS DE MASCOTA",datos)
            self.mostrar_resultado(True,"Citas consultadas exitosamente",self.ventana_cita_mascota)
        else:
            self.mostrar_resultado(False,datos)
            
    def cancelar_cita(self):
        
        self.ventana_cancelar,self.input_id_cita = self.abrir_ventana_input_unico("Cancelar cita","ID cita:",self.cancelar_cita_gui)
        
    def cancelar_cita_gui(self):
        
        self.id_cita = self.input_id_cita.get().upper().strip()
        
        if not self.id_cita:
            messagebox.showwarning("Campo vacío","Este campo no puede estar vacío")
            return
        
        exito,datos = validacion_cancelar_cita(self.citas,self.id_cita)
        
        if exito:
            if messagebox.askyesno("Confirmación","¿Desea cancelar la cita?"):
                exito,datos = ejecutar_cancelacion_cita(self.citas,self.id_cita)
                if exito:
                    self.guardar_cambios()
                self.mostrar_resultado(True,datos,self.ventana_cancelar)
            else:
                self.mostrar_resultado(False,"No se realizo la cancelación de cita")
        else:
            self.mostrar_resultado(False,datos,self.ventana_cancelar)
            
    def registrar_cita(self):
        
        self.ventana_reg_cita = tk.Toplevel(self.ventana)
        self.ventana_reg_cita.title("Registrar Nueva Cita")
        self.ventana_reg_cita.geometry("400x350")
        self.ventana_reg_cita.grab_set()

        tk.Label(
            self.ventana_reg_cita,
            text="🐾 Formulario de Registro",
            font=("Tahoma", 13, "bold"),
        ).pack(pady=12)
        form = ttk.Frame(self.ventana_reg_cita)
        form.pack(padx=20, pady=5, fill="both", expand=True)

        ttk.Label(form, text="ID de la mascota:").grid(
            row=0, column=0, sticky="w", pady=8
        )
        self.input_mascota = ttk.Entry(form, width=25)
        self.input_mascota.grid(row=0, column=1, pady=8, padx=5)

        ttk.Label(form, text="ID servicio:").grid(row=1, column=0, sticky="w", pady=8)
        self.input_servicio = ttk.Entry(form, width=25)
        self.input_servicio.grid(row=1, column=1, pady=8, padx=5)

        ttk.Label(form, text="Fechas:").grid(row=2, column=0, sticky="w", pady=8)
        self.fechas = ttk.Combobox(
            form, values=[ "12/10/2026","13/10/2026","14/10/2026","15/10/2026","16/10/2026","17/10/2026","18/10/2026"], state="readonly", width=23
        )
        self.fechas.grid(row=2, column=1, pady=8, padx=5)
        self.fechas.set("12/10/2026")

        ttk.Label(form, text="Franjas horarias:").grid(row=3, column=0, sticky="w", pady=8)
        self.franjas = ttk.Combobox(form, values=["8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","14:00-15:00","15:00-16:00","16:00-17:00"], state="readonly")
        self.franjas.grid(row=3, column=1, pady=8, padx=5)
        self.franjas.set("8:00-9:00")

        ttk.Button(
            self.ventana_reg_cita,
            text="Guardar Registro",
            command=self.ejecutar_registro_cita_gui,
        ).pack(pady=20)
        
    def ejecutar_registro_cita_gui(self):
        
        id_mascota = self.input_mascota.get().upper().strip()
        
        id_servicio = self.input_servicio.get().upper().strip()
        
        fechas = self.fechas.get()
        
        franjas = self.franjas.get()
        
        if not id_mascota or not id_servicio:
            messagebox.showwarning("Campo vacío","Los campos no pueden estar vacios")
            return
        exito,datos = registrar_cita(self.citas,id_mascota,id_servicio,self.mascotas,self.servicios,fechas,franjas)
        
        if exito:
            self.guardar_cambios()
            self.mostrar_resultado(True,"Se registro la cita correctamente",self.ventana_reg_cita)
            self.etiqueta_estado.config(text="Se registro la cita correctamente")
        else:
            self.mostrar_resultado(False,datos,self.ventana_reg_cita)
            self.etiqueta_estado.config(text="No se regitro la mascota")
        
        
    def cerrar_aplicacion(self):
        if messagebox.askyesno("Salir", "¿Desea cerrar la aplicación?"):
            self.ventana.destroy()

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    try:
        clientes, mascotas, servicios, citas = cargar_datos()
    except (OSError, ValueError, KeyError) as error:
        messagebox.showerror("Error al cargar datos", f"No se pudo leer datos.json: {error}")
    else:
        app = InterfazChikPets(clientes, mascotas, servicios, citas)
        app.ejecutar()
