import unittest
import json
from app import app, db
from models import User


class TestAuthBackend(unittest.TestCase):
    #Pruebas unitarias para el backend de autenticación

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register_success(self):
        #Test: Registro exitoso
        payload = {'username': 'diego', 'email': 'diego@mail.com', 'password': 'pass123'}
        response = self.client.post('/api/register', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['user']['username'], 'carlos')

    def test_login_success(self):
        #Test: Login exitoso
        # Registrar
        self.client.post('/api/register', 
                        data=json.dumps({'username': 'diego', 'email': 'diego@mail.com', 'password': 'pass123'}),
                        content_type='application/json')
        # Login
        response = self.client.post('/api/login',
                                     data=json.dumps({'username': 'diego', 'password': 'pass123'}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['user']['username'], 'diego')

    def test_health_check(self):
        #Test: Health check endpoint
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'ok')


if __name__ == '__main__':
    unittest.main()
