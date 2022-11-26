class Vector:

    # values: list of list of floats (for row vector) or list of lists of single float (for column vector),
    # shape: tuple of 2 integers: (1,n) for a row vector of dimension n or (n,1) for a column vector of dimension n.

    def __init__(self, values):
        self.values = None
        if isinstance(values, int):
            assert values >= 0, f"Value should be positive"
            self.values = []
            for x in range(values):
                self.values.append([float(x)])
            # self.values.append([x for x in range(values)])
        elif isinstance(values, tuple):
            self.values = []
            for x in range(len(values)):
                self.values.append([float(values[x])])
        else:
            self.values = values
            # self.values.append(values)

    def dot(self):
        print('Dot product')

    def T(self):
        print('Vector Transpose')

if __name__ == '__main__':
    print(Vector([1. , 2e-3, 3.14, 5.]).values) # [1.0, 2e-3, 3.14, 5.0]

    print(Vector(4).values) # [[0.0], [1.0], [2.0], [3.0]]

    # print(Vector(-1).values) # This should be an error

    print(Vector((10, 12)).values) # [[10.0], [11.0]]
