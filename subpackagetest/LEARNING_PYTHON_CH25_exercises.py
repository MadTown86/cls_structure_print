import sys

"""
2/12/22 - GD
Part V Exercises
"""


def lfilelist():
    import os
    cwd = os.getcwd()
    for x in os.listdir(cwd):
        print(x)


def getfilename():
    filename = input("Please enter filename ")
    return filename


def countLines(name=None):
    if name is None:
        countLines.name = getfilename()
        file = open(countLines.name, 'r')
        return int(len(file.readlines()))
    else:
        countLines.name = name
        file = open(countLines.name, 'r')
        return int(len(file.readlines()))


def countChars(name=None):
    if name is None:
        name = getfilename()
        file = open(name, 'r')
        return int(len(file.read()))
    else:
        file = open(name, 'r')
        return int(len(file.read()))


def tester(name):
    print(countLines(name))
    print(countChars(name))
    return countLines(name), countChars(name)


if __name__ == '__main__':
    tester("mod1_importtest.py")

