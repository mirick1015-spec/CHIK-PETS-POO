# CHIK & PETS — Proyecto 2 de Programación

Aplicación en Python para administrar **clientes, mascotas, servicios y citas** de un establecimiento de servicios para mascotas. Incluye interfaz gráfica con Tkinter, programa de consola y almacenamiento local en JSON.

## Requisitos

- Python 3 con Tkinter (incluido habitualmente en Python para Windows).
- No se necesitan dependencias externas ni `pip install`.

## Ejecución

1. Descarga o clona el repositorio, manteniendo **todos los archivos en la misma carpeta**.
2. Abre esa carpeta en Visual Studio Code o en una terminal.
3. Para abrir la **interfaz gráfica** ejecuta:

   ```bash
   python gui.py
   ```

4. Para abrir la **consola** ejecuta:

   ```bash
   python consola.py
   ```

5. Para salir, utiliza **Salir** en la GUI o **0** en la consola.

## Organización del código

| Archivo | Función |
|---|---|
| `gui.py` | Interfaz gráfica definitiva (basada en el diseño del equipo). |
| `consola.py` | Menús y acciones en consola. |
| `gestion.py` | Operaciones y reglas de negocio compartidas. |
| `Cliente.py`, `Mascota.py`, `Servicio.py`, `Cita.py` | Clases de programación orientada a objetos. |
| `validaciones_y_datos_iniciales.py` | Validaciones y selección de entradas. |
| `persistencia.py` | Funciones `cargar_datos()` y `guardar_datos()`. |
| `datos.json` | Archivo único que guarda clientes, mascotas, servicios y citas. |

## Persistencia y datos de demostración

- La GUI y la consola usan **el mismo `datos.json`**. No ejecutes ambas a la vez.
- Las operaciones exitosas se guardan y los cambios se recuperan al reiniciar.
- El JSON de entrega contiene **6 clientes, 6 mascotas, 7 servicios y 5 citas** de demostración.
- Si se elimina `datos.json`, el programa inicia con colecciones vacías. Para restaurar los datos de prueba, recupera el archivo original del ZIP o repositorio.
- Si el JSON tiene un formato incorrecto, se muestra un error y no se sobrescribe automáticamente al iniciar.
- La GUI de esta versión presenta fechas predefinidas del **12 al 18 de octubre de 2026**.

## Pruebas rápidas

1. Muestra el listado de clientes, mascotas, servicios y citas.
2. Busca el cliente `1110293559`, mascota `M001`, servicio `S001` y cita `C001`.
3. Intenta registrar un cliente con ID duplicado: debe rechazarse.
4. Intenta reservar la fecha `12/10/2026`, franja `8:00-9:00`: debe rechazarse mientras `C001` esté activa.
5. Intenta eliminar `M001`: debe rechazarse porque tiene historial de citas.
6. Cancela `C001` e intenta volver a cancelarla: el segundo intento debe rechazarse.
7. Cierra y vuelve a ejecutar: verifica que las operaciones aceptadas se conservaron.

**Consejo:** conserva una copia de `datos.json` antes de probar operaciones que cambien información.

## Entrega académica

Acompaña el repositorio con el informe final actualizado, la evidencia de pruebas y el enlace a este repositorio en el documento de entrega.
