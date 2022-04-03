"""
GD - 3/26/2022
This module's purpose is to create an inheritable class for printing class structures and inheritance trees
to give a clearer picture how Python traverses class structure when classes are organized in different ways.
"""
class_tier = 0
class_cont = []

def printerclsfunc(obj):
    """
    This is a printer function that houses the framework for what data you want printed from each class
    :param obj:
    :return:
    """
    global class_tier
    printout = ''
    if hasattr(obj, '__bases__'):
        printout += "\nCLASS INFORMATION"
        printout += "\nClass:: %s is Tier %s" % (obj.__name__, class_tier)
        printout += "\nThe following list contains class methods: " \
                    + str([meth for meth in dir(obj) if not meth.startswith("l")])
        printout += "\nIts SUPER classes are: %s" % [supcls for supcls in obj.__bases__]
        if hasattr(obj, "__subclasses__"):
            printout += "\nThis Classes SUB-CLASSES are: %s" % obj.__subclasses__
        printout += "\nThese are classes already reached: %s" % [contcls for contcls in class_cont]
        return print(printout)
    else:
        printout += "\nINSTANCE INFORMATION"
        printout += "\nClass:: %s is Tier %s" % (obj.__class__, class_tier)
        printout += "\nThe following list contains class methods: " \
                    + str([meth for meth in dir(obj) if not meth.startswith("__")])
        printout += "\nIts SUPER classes are: %s" % [supcls for supcls in obj.__class__.__bases__]
        printout += "\nThese are classes already reached: %s" % [contcls for contcls in class_cont]
        return print(printout)

def treeshredder_recurse(obj):
    """
    This function is passed an instance object and houses the logic for collecting class tree structure data via recursion
    :param obj:
    :return:
    """
    global class_cont
    global class_tier
    if hasattr(obj, "__bases__"):
        if obj.__name__ not in class_cont:
            class_cont.append(obj.__name__)
            printerclsfunc(obj)
            class_tier += 1
            for supscls in range(len(obj.__bases__)):
                treeshredder_recurse(obj.__bases__[supscls])
        else:
            return
    else:
        if obj.__class__.__name__ not in class_cont:
            class_cont.append(obj.__class__.__name__)
            printerclsfunc(obj)
            class_tier += 1
            for suprcls in range(len(obj.__class__.__bases__)):
                treeshredder_recurse(obj.__class__.__bases__[suprcls])
        else:
            return






class Treeshredder():
    """
    This class is built to display a classes tree structure and be inheritable in future classes through _treeshredder
    """
    def _treeshredder__(self):
        """
        This method will make it possible to use dot notation on an instance to print out its class tree hierarchy
        :return:
        """
        return treeshredder_recurse(self)


if __name__ == "__main__":
    """
    Testing Environment
    """


    def test_label(var):
        print("\n\nTEST %s *******************" % var)

    def test1():
        """
        Test printerclsfunc
        :return:
        """
        test_label(1)

        class A:
            pass

        class B(A):
            pass

        class C(B, A):
            pass

        C1 = C()

        return print(printerclsfunc(C1))

    test1()

    def test2():
        test_label(2)

        class E:
            pass

        class F:
            pass

        class D(Treeshredder, E, F):
            pass

        D1 = D()

        D1._treeshredder__()

    test2()
