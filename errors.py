def f(age):
    if age < 18:
        raise ValueError


def func():
    try:
        x = 5/0
        f(19)
    except ValueError:
        print("age must be greater than 18")
    # except ZeroDivisionError:
    #     print("division by zero is forbidden")
    finally:
        print("end")









func()