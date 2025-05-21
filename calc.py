def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Ошибка: деление на ноль!"
    except Exception as e:
        return f"Ошибка: {str(e)}"