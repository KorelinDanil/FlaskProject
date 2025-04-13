import unittest
import datetime
from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Иван Иванов", 1990, "ул. Пушкина, д.10")
        self.homeless_person = Person("Бездомный", 1985)

    def test_initialization(self):
        self.assertEqual(self.person.name, "Иван Иванов")
        self.assertEqual(self.person.yob, 1990)
        self.assertEqual(self.person.address, "ул. Пушкина, д.10")
        self.assertEqual(self.homeless_person.address, "")

    def test_get_age(self):
        current_year = datetime.datetime.now().year
        expected_age = current_year - 1990
        self.assertEqual(self.person.get_age(), expected_age)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), "Иван Иванов")

    def test_set_name(self):
        self.person.set_name("Петр Петров")
        self.assertEqual(self.person.name, "Петр Петров")

    def test_set_address(self):
        self.person.set_address("ул. Лермонтова, д.5")
        self.assertEqual(self.person.address, "ул. Лермонтова, д.5")

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), "ул. Пушкина, д.10")
        self.assertEqual(self.homeless_person.get_address(), "")

    def test_is_homeless(self):
        self.assertFalse(self.person.is_homeless())
        self.assertTrue(self.homeless_person.is_homeless())
        self.homeless_person.set_address("ул. Новая")
        self.assertFalse(self.homeless_person.is_homeless())

if __name__ == '__main__':
    unittest.main()