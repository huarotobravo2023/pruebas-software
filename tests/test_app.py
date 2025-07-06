import pytest
import sys
import os
import tempfile

# Agregar el directorio padre al path para importar app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, init_db, DATABASE

@pytest.fixture
def client():
    """Crea un cliente de pruebas y una base de datos temporal"""
    # Crear archivo temporal para la base de datos de pruebas
    db_fd, temp_db = tempfile.mkstemp()
    app.config['TESTING'] = True
    
    # Usar la base de datos temporal
    import app as app_module
    original_db = app_module.DATABASE
    app_module.DATABASE = temp_db
    
    # Inicializar la base de datos de pruebas
    init_db()
    
    with app.test_client() as client:
        yield client
    
    # Limpiar después de las pruebas
    os.close(db_fd)
    os.unlink(temp_db)
    app_module.DATABASE = original_db

def test_index_page(client):
    """Test que la página principal carga correctamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Mis Notas' in response.data

def test_nueva_nota_get(client):
    """Test que la página de nueva nota carga correctamente"""
    response = client.get('/nueva')
    assert response.status_code == 200
    assert b'Nueva Nota' in response.data

def test_crear_nota(client):
    """Test crear una nueva nota"""
    response = client.post('/nueva', data={
        'titulo': 'Nota de prueba',
        'contenido': 'Contenido de prueba'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Nota creada exitosamente!' in response.data

def test_crear_nota_campos_vacios(client):
    """Test validación de campos obligatorios"""
    response = client.post('/nueva', data={
        'titulo': '',
        'contenido': ''
    })
    
    assert response.status_code == 200
    assert b'Por favor completa todos los campos' in response.data

def test_ver_nota_inexistente(client):
    """Test acceso a nota inexistente"""
    response = client.get('/ver/999', follow_redirects=True)
    assert response.status_code == 200
    assert b'Nota no encontrada' in response.data

def test_app_startup():
    """Test que la aplicación puede iniciarse correctamente"""
    assert app is not None
    assert app.config['SECRET_KEY'] == 'tu_clave_secreta_aqui'
