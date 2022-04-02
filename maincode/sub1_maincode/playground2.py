from maincode.playground import *

def playgroundit():
    filename = input("Enter a filename")
    print(myclient.countLines(filename))
    print(myclient.countChars(filename))

playgroundit()