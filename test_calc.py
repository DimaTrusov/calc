import unittest

def divide(a, b):
    if b == 0:
        raise ValueError("Ошибка: деление на ноль!")
    return a / b

class TestCalculator(unittest.TestCase):

    def test_sum2(self):
        self.assertEqual(2 + 3, 5)
        print("\033[92m[25%]\033[0m")  # Зеленый цвет для вывода

    def test_subtract(self):
        self.assertEqual(10 - 5, 5)
        print("\033[92m[50%]\033[0m")  # Зеленый цвет для вывода

    def test_multiply(self):
        self.assertEqual(3 * 4, 12)
        print("\033[92m[75%]\033[0m")  # Зеленый цвет для вывода

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(-10, 2), -5)
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    print("===== ===== test session start ====")
    print("collecting … collected 4 items")

    # Запускаем тесты
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Рассчитываем процент успешных тестов
    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    passed_tests = total_tests - failed_tests

    # Выводим результат
    success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    print(f"\n[100%]")  # Отображаем 100% в конце
    if failed_tests > 0:
        print(f"\n{failed_tests} tests failed.")
    else:
        print("All tests passed!")