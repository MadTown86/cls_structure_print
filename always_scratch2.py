import always_scratch

class Higher1(always_scratch.ClsBreakDown):
    pass

class Blank1257(Higher1):
    pass

class A(Blank1257):
    pass

class B(A):
    pass

class C(B, A):
    pass


Blank1 = Blank1257()
A1 = A()
B1 = B()
C1 = C()

List1 = [Blank1, A1, B1, C1]
namecont = []
count = 0
ZZ = always_scratch.ClsBreakDown



def valueprinter(obj):
    print("This is what was given to valueprinter:  %s" % obj.__class__)
    if hasattr(obj, "__bases__"):
        #print("This is obj: %s" % obj)
        print("This is obj.__bases__: %s" % obj.__bases__)
        print("This is for class " + str(obj.__class__) + "obj.__class__" + str(obj.__class__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__name__" + str(obj.__class__.__name__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__" + str(obj.__class__.__bases__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0]" + str(obj.__class__.__bases__[0]))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__name__" + str(
            obj.__class__.__bases__[0].__name__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__class__" + str(
            obj.__class__.__bases__[0].__class__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__bases__" + str(
            obj.__class__.__bases__[0].__bases__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__dict__" + str(
            obj.__class__.__bases__[0].__dict__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__dict__.__class__.__bases__" + str(
            obj.__class__.__bases__[0].__dict__.__class__.__bases__))
        print("This is a list of dir(cls) values: %s" % [x for x in dir(obj)])
    else:
        #print("This is obj: %s" % obj)
        print("This is for class " + str(obj.__class__) + "obj.__class__" + str(obj.__class__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__name__" + str(obj.__class__.__name__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__" + str(obj.__class__.__bases__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0]" + str(obj.__class__.__bases__[0]))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__name__" + str(
            obj.__class__.__bases__[0].__name__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__class__" + str(
            obj.__class__.__bases__[0].__class__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__bases__" + str(
            obj.__class__.__bases__[0].__bases__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__dict__" + str(
            obj.__class__.__bases__[0].__dict__))
        print("This is for class " + str(obj.__class__) + "obj.__class__.__bases__[0].__dict__.__class__.__bases__" + str(
            obj.__class__.__bases__[0].__dict__.__class__.__bases__))
        print("This is a list of dir(cls) values: %s" % [x for x in dir(obj)])



def returnit(cls):
    global namecont
    print("\n Class Fed To ReturnIt:: %s" % cls)
    valueprinter(cls)
    print("\n\n")
    if cls not in namecont:
        namecont.append(cls)
        if cls.__class__.__name__ == "type" and cls.__bases__[0] == object:
            print(namecont)
            return print("\n Class:: %s Is A Top Level" % cls.__class__.__name__)
        elif hasattr(cls, "__bases__"):
            for sups in range(len(cls.__bases__)):
                returnit(cls.__bases__[sups])
        else:
            for sup2 in range(len(cls.__class__.__bases__)):
                returnit(cls.__class__.__bases__[sup2])
    else:
        return print("Name in namecont:  %s" % str(namecont))


def printanother(obj):
    global count
    print("Count at tope level %s" % count)
    if obj.__class__ in namecont:
        return


def simplerecur(cls):
    global namecont

    for count in range(len(cls.__class__.__bases)):
        namecont.append(cls.__class__.__name__)

#simplerecur(C1)

#printanother(Higher1)










