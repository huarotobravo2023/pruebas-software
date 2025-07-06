# 📝 Aplicación de Notas Simple con CI/CD

Una aplicación web simple hecha con Flask para tomar notas rápidas con funcionalidades CRUD básicas usando SQLite y pipeline CI/CD completo.

## 🚀 Características

- ✅ **Crear** notas nuevas
- 👁️ **Leer/Ver** notas existentes
- ✏️ **Actualizar/Editar** notas
- 🗑️ **Eliminar** notas
- 💾 Base de datos SQLite local
- 🔄 **CI/CD Pipeline** con GitHub Actions
- 🧪 **Tests automáticos** con pytest
- 🌐 **Despliegue automático** en Render
- 📱 Interfaz responsive y fácil de usar

## 📋 Requisitos

- Python 3.11 o superior
- Flask
- SQLite (incluido con Python)
- Git

## 🛠️ Instalación Local

1. **Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/flask-notas-app.git
cd flask-notas-app
```

2. **Crea un entorno virtual:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

4. **Ejecuta la aplicación:**
```bash
python app.py
```

5. **Abre en el navegador:** `http://127.0.0.1:5000`

## 🧪 Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Test con cobertura
pytest tests/ --cov=app
```

## 🔄 CI/CD Pipeline

### GitHub Actions
- ✅ Tests automáticos en cada push
- ✅ Validación de código
- ✅ Múltiples versiones de Python
- ✅ Deploy automático a producción

### Render Deployment
- 🌐 Despliegue automático desde GitHub
- � Build automático con cada push a main
- 📊 Logs de despliegue en tiempo real

## �📁 Estructura del Proyecto

```
├── app.py                    # Aplicación Flask principal
├── requirements.txt          # Dependencias Python
├── Procfile                  # Configuración para Render
├── .gitignore               # Archivos ignorados por Git
├── notas.db                 # Base de datos SQLite (local)
├── templates/               # Plantillas HTML
│   ├── base.html           # Plantilla base
│   ├── index.html          # Página principal
│   ├── nueva_nota.html     # Crear nota
│   ├── ver_nota.html       # Ver nota
│   └── editar_nota.html    # Editar nota
├── tests/                   # Tests automáticos
│   ├── __init__.py         # Paquete Python
│   └── test_app.py         # Tests principales
└── .github/                # GitHub Actions
    └── workflows/
        └── ci-cd.yml       # Pipeline CI/CD
```

## 🎯 Uso de la Aplicación

1. **Crear una nota**: Haz clic en "Nueva Nota" y completa el formulario
2. **Ver notas**: En la página principal verás todas tus notas
3. **Ver una nota completa**: Haz clic en "Ver" en cualquier nota
4. **Editar una nota**: Haz clic en "Editar" para modificar el contenido
5. **Eliminar una nota**: Haz clic en "Eliminar" (te pedirá confirmación)

## � Configuración GitHub + Render

### 1. Crear repositorio en GitHub:
```bash
# Inicializar Git
git init
git add .
git commit -m "Initial commit"

# Conectar con GitHub
git branch -M main
git remote add origin https://github.com/tu-usuario/flask-notas-app.git
git push -u origin main
```

### 2. Configurar Render:
1. Ve a [render.com](https://render.com)
2. Conecta tu cuenta GitHub
3. Crea un nuevo "Web Service"
4. Selecciona tu repositorio
5. Configuración automática detectada:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### 3. Variables de entorno (opcional):
```
PYTHON_VERSION=3.11.5
```

## 📊 Tests Incluidos

- ✅ Test de carga de página principal
- ✅ Test de creación de notas
- ✅ Test de validación de campos
- ✅ Test de manejo de errores
- ✅ Test de arranque de aplicación

## 💡 Mejoras Futuras

- [ ] Autenticación de usuarios
- [ ] Categorías de notas
- [ ] Búsqueda de notas
- [ ] Exportar notas
- [ ] API REST
- [ ] Notificaciones

## 📝 Comandos Útiles

```bash
# Desarrollo
python app.py

# Tests
pytest tests/ -v

# Cobertura de tests
pytest tests/ --cov=app

# Lint del código
flake8 app.py

# Git workflow
git add .
git commit -m "mensaje"
git push origin main
```

## 🏗️ Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Base de Datos**: SQLite
- **Frontend**: HTML, CSS, Bootstrap
- **Testing**: pytest
- **CI/CD**: GitHub Actions
- **Deploy**: Render
- **Version Control**: Git

---

**Desarrollado con ❤️ usando Flask y mejores prácticas de DevOps**
