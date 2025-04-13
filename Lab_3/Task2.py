import unittest
from Lab_2.Zadacha3 import decrypt


class TestDecryptor(unittest.TestCase):
    def test_single_dot(self):
        """Тестирование случаев с одной точкой"""
        test_cases = [
            ("абра-кадабра.", "абра-кадабра"),
            ("абр......a.", "a"),
            ("1.2.3", "123"),
            (".", ""),
        ]

        for encrypted, expected in test_cases:
            with self.subTest(encrypted=encrypted):
                self.assertEqual(decrypt(encrypted), expected)

    def test_double_dots(self):
        """Тестирование случаев с двойными точками"""
        test_cases = [
            ("абраа..-кадабра", "абра-кадабра"),
            ("абраа..-.кадабра", "абра-кадабра"),
            ("абра--..кадабра", "абра-кадабра"),
            ("абрау...-кадабра", "абра-кадабра"),  # Двойные + одинарные
            ("1..2.3", "23"),
        ]

        for encrypted, expected in test_cases:
            with self.subTest(encrypted=encrypted):
                self.assertEqual(decrypt(encrypted), expected)

    def test_multiple_dots(self):
        """Тестирование случаев с множеством точек"""
        test_cases = [
            ("абра........", ""),
            ("абр......a.", "a"),
            ("1.......................", ""),
            ("...", ""),
            ("абрау.....-кадабра", "абр-кадабра"),
        ]

        for encrypted, expected in test_cases:
            with self.subTest(encrypted=encrypted):
                self.assertEqual(decrypt(encrypted), expected)

    def test_mixed_cases(self):
        """Тестирование смешанных случаев"""
        test_cases = [
            ("абра-кадабра.", "абра-кадабра"),
            ("абраа..-.кадабра", "абра-кадабра"),
            ("абрау...-кадабра", "абра-кадабра"),
            ("1..2.3", "23"),
            ("абр......a.", "a"),
        ]

        for encrypted, expected in test_cases:
            with self.subTest(encrypted=encrypted):
                self.assertEqual(decrypt(encrypted), expected)

    def test_edge_cases(self):
        """Тестирование крайних случаев"""
        test_cases = [
            ("", ""),
            (".", ""),
            ("..", ""),
            ("a", "a"),
            ("a.", "a"),
            ("a..", ""),
            (".a", "a"),
            ("..a", "a"),
        ]

        for encrypted, expected in test_cases:
            with self.subTest(encrypted=encrypted):
                self.assertEqual(decrypt(encrypted), expected)


if __name__ == '__main__':
    unittest.main()