def function_decorator(calculate):
    def add_text(x, y):
        print(f"Here are the results Taha:")
        calculate(x,y)
    return add_text


@function_decorator
def add(x, y):
    print(f"{x} + {y} = {x + y}")


def subtract(x, y):
    print(f"{x} - {y} = {x - y}")


def multiply(x, y):
    print(f"{x} * {y} = {x * y}")


def division(x, y):
    print(f"{x} / {y} = {x / y}")


add(2,4)


