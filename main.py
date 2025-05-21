from calc import calculate

def main():
    print("Введите математическое выражение для вычисления (например, 5 + 1, 7 * 2, 28 / 7).")
    print("Для выхода введите 'q'.")

    while True:
        expression = input("Введите выражение: ")

        if expression.lower() == 'q':
            print("Выход из программы.")
            break

        result = calculate(expression)
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()