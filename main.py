import parser
import sys


def printusage():
    print "Usage: main.py <data_file> <mode>\nMode can be either \"e\" for explicit where the answer is explicitly checked if it is the same in the data file or \"ne\" for non-explicit where your answer and the correct answer are printed out"
    exit(0)


def checkifvalid(args):
    if len(args) < 3:
        printusage()
    if parser.parse(args[1]) == False:
        printusage()
    mode = args[2]
    if mode != "e" and mode != "ne":
        printusage()


def explicitgame():
    while True:
        key = parser.getrandomkey()
        answer = raw_input(key+"?")
        if parser.checkiftrue(key, answer):
            print "Correct! The answer was indeed " + answer
        else:
            print "Incorrect! The answer was " + parser.getcorrectanswer(key)


def nonexplicitgame():
    while True:
        key = parser.getrandomkey()
        answer = raw_input(key+"?")
        print "Your answer was " + answer + ". The correct answer was " + parser.getcorrectanswer(key)

def main():
    argv = sys.argv
    checkifvalid(argv)
    mode = argv[2]
    try:
        if mode == "e":
            explicitgame()
        elif mode == "ne":
            nonexplicitgame()
    except:
        print("\nSee you later!")
        exit(0)


# Start
if __name__ == '__main__':
    main()
