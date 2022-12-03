from vector import Vector

if __name__ == '__main__':

    # # --------------- Example 1 ---------------

    print(Vector(4).values) # [[0.0], [1.0], [2.0], [3.0]]
    print(Vector(4).shape) # (4, 1)

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
