#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    if (a == 2):
        print("{} arument:".format(1))
        print("{}: {}".format(1), sys.argv[1])
    else:
        if (a == 1):
            print("{} aruments.".format(a - 1))
        else:
            print("{} aruments:".format(a - 1))
            for i in range(len(a - 1):
                print("{}: {}".format(i + 1), sys.argv[i + 1])
