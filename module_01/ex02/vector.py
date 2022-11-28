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
            # assert values >= 0, f"Value should be positive"
            self.values = []
            for x in range(values):
                self.values.append([float(x)])
            self.shape = (len(self.values), 1)
        elif isinstance(values, tuple):
            self.values = []
            for x in range(values[0], values[1]):
                self.values.append([float(x)])
            self.shape = (len(self.values), 1)
        else:
            self.values = []
            inc_flag = 0
            if isinstance(values, list):
                for x in range(len(values)):
                    if isinstance(values[x], list):
                        for i in range(len(values[x])):
                            assert isinstance(values[x][i], (int, float)), f"should only construct a list with numbers"
                            values[x][i] = float(values[x][i])
                            inc_flag += 1
                        self.shape = (len(values), 1) if len(values) != 1 else (1, inc_flag)
                    elif isinstance(values[x], (int, float)):
                        self.shape = (1, len(values))
                        assert isinstance(values[x], (int, float)), f"should only construct a list with numbers" 
                        values[x] = float(values[x])
            self.values = values

    def dot(self):
        print('Dot product')

    def T(self):
        print('Vector Transpose')

if __name__ == '__main__':
    # # ------------------------------------
    # print(Vector([1. , 2e-3, 3.14, 5]).shape) # [1.0, 2e-3, 3.14, 5.0]

    print(Vector(4).values) # [[0.0], [1.0], [2.0], [3.0]]
    print(Vector(4).shape)
    # # print(Vector(-1).values) # This should be an error
    # print(Vector([[0.0, 1.0, 2.0, 5]]).values) # [[0.0, 1.0, 2.0, 5.0]]
    # print(Vector([[0.0], [1.0], [2.0], [3.0]]).values) # [[0.0], [1.0], [2.0], [3.0]]
    # print(Vector((10, 12)).values) # [[10.0], [11.0]]
    # print(Vector((1, 1)).values) # []
    # print(Vector((4, 7.1)).values) # Cannot interpret floats as int

    # # ------------------------------------
    # Column vector of shape (n, 1)
    # print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
    # Expected output
    # (4,1)

    # print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    # Expected output
    # [[0.0], [1.0], [2.0], [3.0]]

    # Row vector of shape (1, n)
    # print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
    # Expected output
    # (1,4)

    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v1.shape)
    # # Expected output
    # # [[0.0, 1.0, 2.0, 3.0]]

    # # Example 1:
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)
    # Expected output:
    # (4,1)
    
