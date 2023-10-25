from time import time

from self_practice.decorator import design


def big_list(num):
    double = []
    for i in range(num):
        double.append(i * 2)
    return double

def designer(v):
    print("=======")
    v()
    print("+++++++")
    return v

@designer
def generator_func(n):
    for y in range(n):
        yield y

x = range(100)
print(x)


print((big_list(20)))
a = generator_func(200)
print(next(generator_func(20)))


def wrap(*args, **kwargs):
    time1 = time()
    result = fn(*args, **kwargs)
    time2 = time()
    print(f" {time2 - time1} ")