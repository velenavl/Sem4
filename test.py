# a, b, *c = (1, 2, 3, 4, 5)
# d, e, g = c

# print(a, b, c)
# print(d, e, g)

# def test(a, b, c):
#     return a, b, c


# values = [1, 2, 3]
# print(test(*values))


def new_test(*args, **kwargs):
    a, b, *_ = args
    print(a, b)
    print(kwargs['res'], kwargs['reverse'])


new_test(1, 2, 3, 4, 'f', 'g', res=True, reverse='Yes')

# *a, b, c = (1, 2, 3, 4, 5, 6)
# print(a, b, c)
