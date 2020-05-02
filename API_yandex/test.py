import unittest
import main

class TestSecretaryProgram(unittest.TestCase):

    def test_translate_ru_to_eng(self):
        translate = main.translate_to_file("Я люблю программирование", "ru-en")
        self.assertEqual(translate, 'I love programming')
        print('Результат перевода с русского на английский правильный')

    def test_translate_ru_to_es(self):
        translate = main.translate_to_file("Я люблю программирование", "ru-es")
        self.assertEqual(translate, 'Me encanta la programación')
        print('Результат перевода с русского на испанский правильный')

    def test_translate_fr_to_ru(self):
        translate = main.translate_to_file("J'aime la programmation", "fr-ru")
        self.assertEqual(translate, 'Я люблю программирование')
        print('Результат перевода с французского на русский правильный')

    def test_translate_status_code(self):
        translate_status_code = main.translate_to_file_status_code("Я люблю программирование", "fr-ru")
        self.assertEqual(translate_status_code, 200)
        print('Код ответа соответствует 200')

if __name__ == '__main__':
    unittest.main()
