from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce

if __name__ == '__main__':
    # function = lambda x: x + 1
    # iterable = [1, 2, 3]

    # ft_map(function_to_apply = None, iterable = iterable)
    # list(ft_map(function_to_apply = None, iterable = iterable)) # type: ignore

    # x = [1, 2, 3, 4, 5]
    # print(ft_map(lambda dum: dum + 1, x)) # <generator object ft_map at 0x7f708faab7b0> # The adress will be different
    # print(list(ft_map(lambda t: t + 1, x))) # type: ignore # [2, 3, 4, 5, 6]


    # ft_filter(lambda dum: not (dum % 2), x) # <generator object ft_filter at 0x7f709c777d00> # The adress will be different
    # ft_filter(function_to_apply = None, iterable = iterable)
    # list(ft_filter(function_to_apply = None, iterable = iterable)) # type: ignore

    # ft_reduce(None, iterable = iterable)
    # ft_reduce(function, None)

    # list(ft_map(lambda x: x + 2, [])) # type: ignore # []
    # list(ft_map(lambda x: x + 2, [1])) # type: ignore # [3]
    # list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5])) # type: ignore # [1, 4, 9, 16, 25]
    # list(ft_filter(lambda x: x <= 1, [])) # type: ignore # []
    # ft_reduce((lambda x, y: x + y), [1]) # 1
    # ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]) # 24

    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    print(ft_reduce(lambda u, v: u + v, lst)) # 'Hello world'

