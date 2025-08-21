import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario, si existe."""
        try:
            if not os.path.exists(self.archivo):
                with open(self.archivo, "w") as f:
                    f.write("")  # Crea el archivo vacío si no existe
                print("[INFO] Archivo de inventario creado.")
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    try:
                        nombre, cantidad = linea.strip().split(",")
                        self.productos[nombre] = int(cantidad)
                    except ValueError:
                        print(f"[ADVERTENCIA] Línea corrupta ignorada: {linea.strip()}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"[ERROR] No se pudo leer el archivo: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, "w") as f:
                for nombre, cantidad in self.productos.items():
                    f.write(f"{nombre},{cantidad}\n")
        except PermissionError:
            print("[ERROR] No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"[ERROR] Error inesperado al guardar: {e}")

    def agregar_producto(self, nombre, cantidad):
        """Agrega un producto nuevo o aumenta su cantidad."""
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        self.guardar_inventario()
        print(f"[OK] Producto '{nombre}' agregado/actualizado correctamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        try:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"[OK] Producto '{nombre}' eliminado del inventario.")
        except KeyError:
            print(f"[ERROR] El producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self):
        """Muestra los productos del inventario."""
        if not self.productos:
            print("[INFO] El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for nombre, cantidad in self.productos.items():
                print(f"{nombre}: {cantidad}")
            print("-------------------------")
