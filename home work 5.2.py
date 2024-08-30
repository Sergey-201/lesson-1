while True:

        n1 = float(input("Введите первое число: "))

        operation = input("Введите действие (+, -, *, /): ")

        n2 = float(input("Введите второе число: "))

        match operation:
            case '+':
                result = n1 + n2
            case '-':
                result = n1 - n2
            case '*':
                result = n1 * n2
            case '/':
                if n2 == 0:
                    print("Деление на ноль не возможно!")
                else:
                    result = n1 / n2

        if operation in ['+', '-', '*', '/'] and not (operation == '/' and n2 == 0):

            print(f"Результат: {result}")
        continue_ = input("( для продолжения введите: y, для завершения введите: q  ): ")

        if continue_ == 'q':
            print("Работа завершена.")
            break