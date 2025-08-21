
---

#  Manipulación de Archivos y Manejo de Excepciones

# 🗂️ Sistema de Gestión de Inventarios Mejorado

Este proyecto es una **versión mejorada** del sistema de gestión de inventarios desarrollado anteriormente.
La mejora principal consiste en la **persistencia de datos en archivos** y el **manejo robusto de excepciones**, lo que permite un sistema más realista, resiliente y profesional.

---

#  Mejoras Respecto al Inventario Anterior

## Persistencia de Datos

* Los productos se guardan en un archivo (`inventario.txt`).
* Al iniciar el programa, los datos se cargan automáticamente.
* Ya no se pierde información al cerrar el programa.

## Manejo de Excepciones

* Control de errores al abrir, leer y escribir archivos:

  * `FileNotFoundError` → crea el archivo si no existe.
  * `PermissionError` → muestra un error sin que el programa se cierre.
  * Líneas corruptas en el archivo → se ignoran con advertencia.

## 📌 Interfaz de Usuario Mejorada

* Mensajes claros de éxito o fallo al agregar, eliminar o mostrar productos.
* Notificación cuando el inventario está vacío o un producto no existe.

## Organización del Código

* Separación en dos módulos:

  * `inventario.py` → lógica de negocio y manejo de archivos.
  * `main.py` → menú interactivo en consola.
* Uso de `with open(...)` para mayor seguridad en la manipulación de archivos.

---

#  Ejemplo de Uso

### Agregar productos

```
Nombre del producto: Lápiz  
Cantidad: 50  
[OK] Producto 'Lápiz' agregado/actualizado correctamente.
```

### Mostrar inventario

```
--- Inventario Actual ---
Lápiz: 50
-------------------------
```

### Eliminar producto

```
Nombre del producto a eliminar: Lápiz  
[OK] Producto 'Lápiz' eliminado del inventario.
```

---

#  Pruebas de Robustez

* **Archivo inexistente** → se crea automáticamente.
* **Archivo corrupto** (ejemplo: `productoX,abc`) → se ignora la línea con advertencia.
* **Sin permisos de escritura** → muestra error sin interrumpir la ejecución.

---

# Conclusión

Este sistema aplica conceptos de:

* **Persistencia con archivos en Python**
* **Manejo de excepciones** (`try`, `except`, `finally`)
* **Organización modular del código**
* **Interacción con el usuario en consola**

 Demuestra cómo un proyecto básico puede evolucionar hacia una aplicación **más realista, resiliente y mantenible**.

---

¿Quieres que le agregue al README también una **sección inicial con instrucciones de instalación y ejecución paso a paso** (para que tu profe pueda correrlo sin problemas)?

