def ft_map(function_to_apply, iterable):
    """ Map the function to all elements of the iterable.
        @function_to_apply: a function taking an iterable.
        @iterable: an iterable object (list, tuple, iterator).
        @return An iterable. None if the iterable can not be used by the function.
    """
    if not hasattr(iterable, '__iter__'): return None
    return (function_to_apply(i) for i in iterable)
