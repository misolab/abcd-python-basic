
a = 10


def show_a():
    # global a
    a = 3
    print("[show_a] a is " + str(a))


print("a is " + str(a))
show_a()
print("a is " + str(a))


def multi_return():
    return 'a', 'b', 'c'


A, B, C = multi_return()
print("%c %c %c" % (A, B, C))


def abcd(a='가', b='나', c='다', d='라'):
    def merge():
        return a + b + c + d

    print("merge - " + str(merge()))


abcd()
abcd(1, 2, 3, 4)
abcd('a', 'b', 'c', 'd')


def to_str_by_numeric(int_value: int, float_value: float) -> str:
    return str(int_value + float_value)


print("to_str_by_numeric(10, 11.11) : " + to_str_by_numeric(10, 11.11))


def func_param(a, b, param_func):
    msg = param_func(a, b)
    print("func_param - " + msg)


func_param(10, 11.11, to_str_by_numeric)

func_param(100, 110.11, lambda la, lb: str(la + lb))

