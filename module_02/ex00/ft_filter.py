def ft_filter(function_to_apply, iterable):
    """ Filter the result of function apply to all elements of the iterable.
        @function_to_apply: a function taking an iterable.
        @iterable: an iterable object (list, tuple, iterator).
        @return An iterable. None if the iterable can not be used by the function.
    """
    if not hasattr(iterable, '__iter__'):
        return None
    if not hasattr(function_to_apply, '__call__'):
        return None
    result = []
    for i in iterable:
        if function_to_apply(i):
            result.append(i)
    return result