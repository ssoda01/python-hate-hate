def g(data):
    return data + 1


def f(x):
    # breakpoint()
    lst = []
    for i in range(x):
        val = g(i)
        lst.append(val)
    return lst


ret = f(3)
print(ret)