from subpackagetest.LEARNING_PYTHON_CH25_exercises import *

def myclienter():
    filename = input("Please enter a filename:  ")
    print("From Tester  " + str(countLines(filename)),
          str(countChars(filename)))

myclienter()