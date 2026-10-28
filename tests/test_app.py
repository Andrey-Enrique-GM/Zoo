import pytest
import os
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
from app import app, db, Chihuahua



@pytest.fixture(autouse=True)
def setup_database():
    """Configura Flask en modo testing y crea las tablas en memoria antes de cada test"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


def test_get_all_chihuahuas():
    """Prueba que verifica si se pueden obtener elementos cuando la base de datos tiene registros"""

    with app.app_context():
        nuevo_chihuahua = Chihuahua(
            tipo='Chihuahua Cabezas de Manzana',
            descripcion='Ejemplo de prueba',
            imagen='images/test.png'
        )
        db.session.add(nuevo_chihuahua)
        db.session.commit()

    # Realiza una petición GET a la ruta principal
    with app.test_client() as client:
        response = client.get('/')
        
        # Resultado obtenido
        assert response.status_code == 200

    with app.app_context():
        chihuahuas_en_db = Chihuahua.query.all()
        
        actual_result = len(chihuahuas_en_db)
        expected_result = 1

        # Verificamos que hay mínimo un elemento en la DB
        assert actual_result >= expected_result
