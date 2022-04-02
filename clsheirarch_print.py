"""

"""
import timeit
count = 0
cls_table = ['object']

def cls_recurclimb(cls, base=None):
    global cls_table
    global count
    if base:
        print("BASE CLASS 1 PRIOR: %s " % str(base))
    cls_table.append(cls.__dict__._class__.__name__)
    print(str(cls.__class__))
    print("'__dict__' CONTENTS:")
    for cls_key in cls.__dict__.keys():
        print("KEY:: (%s) :::: VALUE:: (%s)" % (cls_key, cls.__dict__[cls_key]))
    #for cls_dirval in [x for x in dir(cls) if not x.startswith('_')]:
        #print("CLASS METHOD dir() CONTENTS:: VALUE:: (%s) ::::: VALUE:: (%s)" % (dir(cls).index(cls_dirval), cls_dirval))

    for sup_cls in [x for x in cls.__class__.__bases__]:
        if sup_cls in cls_table:
            continue
        else:
            cls_recurclimb(sup_cls, cls)




class ClassHierarchyPrint:

    def list_attributes(self):
        return cls_recurclimb(self)


if __name__ == '__main__':

    class A(ClassHierarchyPrint):
        def __init__(self, var1):
            super().__init__()
            self.var1 = var1

        def updatevar1(self, arg, *vargs, **kwargs):
            self.var1 = arg


    class B(A):
        def __init__(self, var2):
            super().__init__(self)
            self.var2 = var2


    class C(B, A, ClassHierarchyPrint):
        def __init__(self):
            super().__init__(self)
            self.var3 = None

        def set_var3(self, var3):
            self.var3 = var3


    class D(C, B, A, ClassHierarchyPrint):
        def __init__(self):
            super().__init__()
            self.var5 = None
            self.var4 = None

        def set_var3(self, var3, var4=None, *vargs, **kwargs):
            C.set_var3(self, var3)
            self.var4 = var4

        def updatevar1(self, arg, var5=None, *vargs, **kwargs):
            A.updatevar1(self, arg)
            self.var5 = var5


    AX = A("var1")
    AX1 = B("var2")
    CX3 = C()
    CX3.set_var3("var3")
    DX3 = D()
    DX3.updatevar1("Var1D", "Var5")
    DX3.updatevar1("var1D")

    DX3.list_attributes()




