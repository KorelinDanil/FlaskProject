import unittest
from Lab_2.Zadacha7 import app, finance_data


class TestFinanceApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Инициализация тестовых данных"""
        cls.test_data = {
            2023: {
                10: {
                    15: 500,
                    16: 1000
                },
                11: {
                    1: 200
                }
            },
            2024: {
                1: {
                    1: 100
                }
            }
        }

        # Заполняем storage тестовыми данными
        finance_data.update(cls.test_data)

    def setUp(self):
        """Создаем тестовый клиент перед каждым тестом"""
        self.client = app.test_client()
        self.client.testing = True

    def test_add_endpoint_valid(self):
        """Тестирование /add/ с валидными данными"""
        test_cases = [
            ('/add/20231017/300', 'Добавлена трата 300 руб. на дату 17.10.2023'),
            ('/add/20240102/1500', 'Добавлена трата 1500 руб. на дату 2.1.2024'),
            ('/add/20231231/9999', 'Добавлена трата 9999 руб. на дату 31.12.2023')
        ]

        for url, expected in test_cases:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertIn(expected, response.get_data(as_text=True))


    def test_calculate_year_endpoint(self):
        """Тестирование /calculate/<year>"""
        test_cases = [
            ('/calculate/2023', 'Суммарные траты за 2023 год: 1700 руб.'),
            ('/calculate/2024', 'Суммарные траты за 2024 год: 100 руб.'),
            ('/calculate/2025', 'Суммарные траты за 2025 год: 0 руб.')
        ]

        for url, expected in test_cases:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertIn(expected, response.get_data(as_text=True))
    def test_calculate_month_endpoint(self):
        """Тестирование /calculate/<year>/<month>"""
        test_cases = [
            ('/calculate/2023/10', 'Суммарные траты за 10.2023: 1500 руб.'),
            ('/calculate/2023/11', 'Суммарные траты за 11.2023: 200 руб.'),
            ('/calculate/2023/12', 'Суммарные траты за 12.2023: 0 руб.')
        ]

        for url, expected in test_cases:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertIn(expected, response.get_data(as_text=True))

    def test_empty_storage(self):
        """Тестирование с пустым storage"""
        # Сохраняем оригинальные данные
        original_data = finance_data.copy()

        # Очищаем storage
        finance_data.clear()

        test_cases = [
            ('/calculate/2023', 'Суммарные траты за 2023 год: 0 руб.'),
            ('/calculate/2023/10', 'Суммарные траты за 10.2023: 0 руб.'),
            ('/calculate/2024/1', 'Суммарные траты за 1.2024: 0 руб.')
        ]

        for url, expected in test_cases:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertIn(expected, response.get_data(as_text=True))

        # Восстанавливаем данные
        finance_data.update(original_data)

if __name__ == '__main__':
    unittest.main()