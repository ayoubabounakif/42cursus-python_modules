class Vector:

    # values: list of list of floats (for row vector) or list of lists of single float (for column vector),
    # shape: tuple of 2 integers: (1,n) for a row vector of dimension n or (n,1) for a column vector of dimension n.

    def __checkvalidity(self, values):
        if isinstance(values, int):
            if not values >= 0: raise ValueError("value should be positive")
        if isinstance(values, tuple):
            if not len(values) == 2: raise ValueError("tuple should be of form of range(a, b)")
            if not (isinstance(values[0], int) and isinstance(values[1], int)): raise ValueError("values should be integers.") 
            if not values[0] <= values[1]: raise ValueError("range(a, b) expect: a < b")
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
            # check if values is a list of list of floats
            if any(isinstance(x, list) for x in values):
                self.values = [list(map(float, sublist)) for sublist in values]
                self.shape = (len(self.values), len(self.values[0]))
            else:
                self.values = values
                self.shape = (len(values), 1)

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
    
    def T(self):
        result = []
        # print (self.values[0])
        # print (len(self.values[0]))
        for x in range(len(self.values[0])):
            result.append([self.values[y][x] for y in range(len(self.values))])
            # print(self.values[0][x])
        return Vector(result)

    # x . y = [x1 ... xn] * [y1 ... yn] = x1 . y1 + ... + xn . yn
    def dot(self, other):
        self.__error(other, "Vector", "dot")
        result = 0
        if len(self.values[0]) == 1:
            for x in range(len(self.values)):
                result += self.values[x][0] * other.values[x][0]
        elif len(self.values) == 1:
            for x in range(len(self.values[0])):
                result += self.values[0][x] * other.values[0][x]
        return result
        


if __name__ == '__main__':

    print()

    # # --------------- Example 1 ---------------

    # print(Vector(4).values) # [[0.0], [1.0], [2.0], [3.0]]
    # print(Vector(4).shape) # (4, 1)

    # print(Vector((2, 4)).values) # [[2.0], [3.0]]
    # print(Vector((2, 4)).shape) # (2, 1)

    # print(Vector([[1, 2, 3], [4, 5, 6]]).values) # [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    # print(Vector([[1, 2, 3], [4, 5, 6]]).shape) # (2, 3)

    # v = Vector(4)
    # v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
    # print((v + v2).values) # [[1.0], [2.0], [3.0], [4.0]]

    # print((v - v2).values != (v2 - v).values) # True


    # # --------------- Example 2 ---------------

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


    # # --------------- Example 3 ---------------

    # print(Vector([1. , 2e-3, 3.14, 5.]).values) # [1.0, 0.002, 3.14, 5.0]
    # print(Vector(4).values) # [[0.0], [1.0], [2.0], [3.0]]
    # # Vector(-1) # ValueError: should only create a Vector with a positive integer
    # print(Vector((10, 12)).values) # [[10.0], [11.0]]
    # # print(Vector((3, 1)).values) # ValueError: range(a, b) expect: a < b
    # print(Vector(0).values) # []
    # print(Vector((1, 1)).values) # []
    # print(Vector((4, 7.1)).values) # ValueError: values should be integers.


    # # --------------- Example 4 ---------------
    # # built-in method __add__, __radd__, __sub__ and __rsub__

    # print(Vector(4) / 2)
    # print(Vector(4) / 3.14)
    # print(Vector(4) / 0) # ValueError: should only divide a Vector to a non-zero scalar
    # print(Vector(4) / None) # NotImplementedError: should only divide a Vector to a scalar
    # print(3 / Vector(3)) # NotImplementedError: should only divide a Vector to a scalar


    # # ------------- Subjects Tests ------------

    # # -------

    # # Column vector of shape (n, 1)
    # print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape) # (4,1)
    # print(Vector([[0.0], [1.0], [2.0], [3.0]]).values) # [[0.0], [1.0], [2.0], [3.0]]

    # # -------

    # # Row vector of shape (1, n)
    # print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape) # (1,4)
    # print(Vector([[0.0, 1.0, 2.0, 3.0]]).values) # [[0.0, 1.0, 2.0, 3.0]]

    # # -------

    # # Example 1:
    # v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    # print(v1.shape) # (4,1)
    # print(v1.T()) # Vector([[0.0, 1.0, 2.0, 3.0]]
    # print(v1.T().shape)


    # # Example 2:
    # v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    # print(v2.shape)
    # print(v2.T()) # Vector([[0.0], [1.0], [2.0], [3.0]])
    # print(v2.T().shape) # (4, 1)
    

    # # -------

    # # Example 3:
    # v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    # v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    # print(v1.dot(v2)) # 18.0

    # v3 = Vector([[1.0, 3.0]])
    # v4 = Vector([[2.0, 4.0]])
    # print(v3.dot(v4)) # 13.0 ??????? -- Manual calculation was 14.0
