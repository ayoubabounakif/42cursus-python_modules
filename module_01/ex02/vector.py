class Vector:

    # values: list of list of floats (for row vector) or list of lists of single float (for column vector),
    # shape: tuple of 2 integers: (1,n) for a row vector of dimension n or (n,1) for a column vector of dimension n.

    def __checkvalidity(self, values):
        if isinstance(values, int):
            assert values >= 0, f"Value should be positive"
        if isinstance(values, tuple):
            assert len(values) == 2, f"Tuple should be of form of range(a, b)"
            assert isinstance(values[0], int) and isinstance(values[1], int), f"Values should be integers."
            assert values[0] <= values[1], f"range(a, b) expect: a < b"
        else:
            pass

    def __init__(self, values):
        self.__checkvalidity(values)
        if isinstance(values, int):
            self.values = [[float(x)] for x in range(values)]
            self.shape = (values, 1)
        elif isinstance(values, tuple):
            self.values = [[float(x)] for x in range(values[0], values[1])]
            self.shape = (values[1] - values[0], 1)
        else:
            self.values = [list(map(float, sublist)) for sublist in values]
            self.shape = (len(self.values), len(self.values[0]))

    def __error(self, other, type, op):
        if (type == "Vector"):
            if not isinstance(other, Vector): raise NotImplementedError(f"should only {op} a Vector to a Vector")
            if not self.shape == other.shape: raise ValueError(f"should only {op} a Vector of same shape")
        elif (type == "scalar"):
            if not isinstance(other, (int, float)): raise NotImplementedError(f"should only {op} a Vector to a scalar")
            if (op == "divide" and other == 0): raise ValueError(f"should only {op} a Vector to a non-zero scalar")

    def __add__(self, other):
        self.__error(other, "Vector", "add")
        result = []
        for x in range(len(self.values)):
            result.append([self.values[x][0] + other.values[x][0]])
        return Vector(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        self.__error(other, "Vector", "subtract")
        result = []
        for x in range(len(self.values)):
            result.append([self.values[x][0] - other.values[x][0]])
        return Vector(result)
    
    def __rsub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        self.__error(other, "scalar", "divide")
        result = []
        for x in range(len(self.values)):
            result.append([self.values[x][0] / other])
        return Vector(result)
    
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    
    def __mul__(self, other):
        self.__error(other, "scalar", "multiply")
        result = []
        for x in range(len(self.values)):
            result.append([self.values[x][0] * other])
        return Vector(result)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return f"Vector({self.values})"
    
    def __repr__(self):
        return f"Vector({self.values})"


if __name__ == '__main__':

    print(Vector(4).values) # [[0.0], [1.0], [2.0], [3.0]]
    print(Vector(4).shape) # (4, 1)

    print(Vector((2, 4)).values) # [[2.0], [3.0]]
    print(Vector((2, 4)).shape) # (2, 1)

    print(Vector([[1, 2, 3], [4, 5, 6]]).values) # [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    print(Vector([[1, 2, 3], [4, 5, 6]]).shape) # (2, 3)

    print(Vector([[1, 2, 3], [4, 5, 6]]).values[0]) # [1.0, 2.0, 3.0]
    print(Vector([[1, 2, 3], [4, 5, 6]]).values[0][0]) # 1.0

    # v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    # v2 = Vector([[0.0], [1.0], [2.0], [0.0]])

    # v3 = Vector([[0.0, 1.0, 2.0, 3.0]])
    # v4 = Vector([[0.0, 1.0, 1.0, 0.0]])

    # try:
    #     print(v1.__add__(v2).values)
    #     print(v1.__sub__(v2).values)
    #     print(v1.__mul__(0).values)
    #     print(v1.__truediv__(5).values)
    # except Exception as error:
    #     print(error)
        
    # try:
    #     print(v3.__add__(v4).values)
    #     print(v3.__sub__(v4).values)
    #     print(v3.__mul__(0).values)
    #     print(v3.__truediv__(4).values)
    # except Exception as error:
    #     print(error)


    
    
