import unittest
from app import create_app

class TestExecuteCode(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_timeout(self):
        response = self.app.post('/execute', data={'code': 'while True: pass', 'timeout': 1})
        self.assertEqual(response.status_code, 408)

    def test_invalid_data(self):
        response = self.app.post('/execute', data={'code': '', 'timeout': 35})
        self.assertEqual(response.status_code, 400)

    def test_valid_execution(self):
        response = self.app.post('/execute', data={'code': 'print(2+2)', 'timeout': 3})
        self.assertIn('4', response.json['stdout'])
