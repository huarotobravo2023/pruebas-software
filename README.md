# 📝 Aplicación de Notas Simple

Una aplicación web simple hecha con Flask para tomar notas rápidas con funcionalidades CRUD básicas usando SQLite.

## 🚀 Características

- ✅ **Crear** notas nuevas
- 👁️ **Leer/Ver** notas existentes
- ✏️ **Actualizar/Editar** notas
- 🗑️ **Eliminar** notas
- 💾 Las notas se guardan en una base de datos SQLite local
- 📱 Interfaz responsive y fácil de usar

## 📋 Requisitos

- Python 3.6 o superior
- Flask
- SQLite (incluido con Python)

## 🛠️ Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta la aplicación:
```bash
python app.py
```

3. Abre tu navegador y ve a: `http://127.0.0.1:5000`

## 📁 Estructura del Proyecto

```
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias
├── notas.db           # Base de datos SQLite (se crea automáticamente)
└── templates/         # Plantillas HTML
    ├── base.html      # Plantilla base
    ├── index.html     # Página principal
    ├── nueva_nota.html # Formulario para crear notas
    ├── ver_nota.html  # Vista de una nota específica
    └── editar_nota.html # Formulario para editar notas
```

## 🎯 Uso

1. **Crear una nota**: Haz clic en "Nueva Nota" y completa el formulario
2. **Ver notas**: En la página principal verás todas tus notas
3. **Ver una nota completa**: Haz clic en "Ver" en cualquier nota
4. **Editar una nota**: Haz clic en "Editar" para modificar el contenido
5. **Eliminar una nota**: Haz clic en "Eliminar" (te pedirá confirmación)

## 💡 Notas

- Las notas se guardan automáticamente en `notas.db` (SQLite)
- La base de datos se crea automáticamente al ejecutar la aplicación
- La aplicación se ejecuta en modo debug para desarrollo
- Es una aplicación simple, perfecta para uso local y personal
