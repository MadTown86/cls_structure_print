class A:
    pass

class B(A):
    pass

class C(B, A):
    pass

A1 = A()
B1 = B()

L1 = [A1, B1, A, B]
objtest1 = A1.__class__.__base__()

print(type(objtest1))