import unittest
import main
import sys
from contextlib import contextmanager
from io import StringIO

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestSecretaryProgram(unittest.TestCase):

    # проверка на вывод
    def test_one_document(self):
        with captured_output() as (out, err):
            main.all_document([{
                "type": "insurance",
                "number": "10006",
                "name": "Аристарх Павлов"
            }])
            output = out.getvalue().strip()
            self.assertEqual(output, 'insurance 10006 Аристарх Павлов')

    # проверка на перенос строки
    def test_all_document(self):
        with captured_output() as (out, err):
            main.all_document(main.documents)
            output = out.getvalue().strip()
            self.assertEqual(output, 'passport 2207 876234 Василий Гупкин\ninvoice 11-2 Геннадий Покемонов\ninsurance 10006 Аристарх Павлов')

    # проверка на вывод исключения KeyError если нет строки NAME
    def test_get_exception_name_people(self):
        with self.assertRaises(KeyError):
            main.all_document([{
                "type": "invoice",
                "number": "11-2",
            }])

    # проверка на вывод имен
    def test_name_people(self):
        with captured_output() as (out, err):
            main.name_people(main.documents)
            output = out.getvalue().strip()
            self.assertEqual(output, 'Василий Гупкин\nГеннадий Покемонов\nАристарх Павлов')


if __name__ == '__main__':
    unittest.main()
