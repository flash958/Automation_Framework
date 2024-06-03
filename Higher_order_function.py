def add1(a, b):
    return (a + b)


def double(add1):
    def inner(a,b):
        return add1(a,b) * 2

    return inner


double_add=double(add1)
print(double_add(3,2))

print(add1(2,2))