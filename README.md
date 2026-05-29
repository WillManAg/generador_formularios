# 🔧 IT Documents — Generador Dinámico de Formularios

¡Bienvenido a **IT Documents**! Esta es una aplicación web robusta, modular y de código abierto desarrollada en **Python 3 y Django**, diseñada específicamente para automatizar la gestión y confección de documentación repetitiva en departamentos de soporte e infraestructura IT.

El proyecto destaca por su arquitectura **100% dinámica**, permitiendo a los administradores del sistema dar de alta nuevas plantillas de Microsoft Word (`.docx`) y configurar sus respectivas preguntas directamente desde el panel de control, sin necesidad de modificar una sola línea de código fuente.

---

## ✨ Características Clave

* **Motor de Relleno Dinámico:** Integración con `docxtpl` (Jinja2) para inyectar datos en variables de archivos Word en tiempo de ejecución.
* **Procesamiento en Memoria RAM:** El documento final se genera en un buffer de bytes (`io.BytesIO`) y se sirve directamente como descarga al navegador, evitando acumular archivos temporales innecesarios en el servidor.
* **Interfaz Fluida Estilo Asistente (Wizard):** Frontend minimalista e interactivo. Permite interactuar con el teclado (avanzar con la tecla `Intro` y autoenfoque del siguiente campo) para maximizar la velocidad del técnico de IT.
* **Panel de Administración Premium:** Interfaz de gestión moderna y estilizada gracias a la integración de la biblioteca open-source `Django Unfold` (basada en Tailwind CSS).
* **Localización Completa:** Entorno configurado íntegramente en español.

---

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.9+ & Django 4.2+
* **Procesamiento de Documentos:** `docxtpl` (Python-docx-template) & `io` (BytesIO)
* **Frontend:** HTML5, CSS3 Nativos (Apple System Fonts) y JavaScript Vanilla (Lógica de control por teclado).
* **Base de Datos:** SQLite3 (Entorno local de desarrollo).
* **Estilos del Administrador:** Django Unfold (Tailwind CSS).

---

## 📂 Estructura del Proyecto

```text
generador_formularios/
│
├── config/                  # Ajustes centrales del proyecto Django
├── formularios/             # Aplicación principal de gestión
│   ├── plantillas_origen/   # Almacenamiento de archivos .docx base (ficticios)
│   ├── templates/           # Vistas HTML (Landing, Listado, Detalle Asistente)
│   ├── models.py            # Diseño relacional (Plantilla Documento 1 ─── N Campos)
│   └── views.py             # Lógica de negocio y motor de renderizado del Word
├── db.sqlite3               # Base de datos local (Ignorada en Git)
└── .gitignore               # Configuración de exclusión de archivos (entorno virtual y DB)