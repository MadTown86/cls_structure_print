import myclient

def playgroundit():
    filename = input("Enter a filename")
    print(myclient.countLines(filename))
    print(myclient.countChars(filename))

playgroundit()