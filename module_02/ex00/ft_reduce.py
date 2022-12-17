def ft_reduce(function_to_apply, iterable):
    """ Apply function of two arguments cumulatively.
        @function_to_apply: a function taking an iterable.
        @iterable: an iterable object (list, tuple, iterator).
        @return A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    if not hasattr(iterable, '__iter__'):
        return None
    if not hasattr(function_to_apply, '__call__'):
        return None
    if len(iterable) == 0:
        return None
    result = iterable[0]
    for i in range(1, len(iterable)):
        result = function_to_apply(result, iterable[i])
    return result
