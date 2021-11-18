#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = sys.argv
    if (len(a) == 2):
        print("{} arument:".format(1))
        print("{}:".format(1), a[1])
    else:
        if (len(a) == 1):
            print("{} aruments.".format(len(a) - 1))
        else:
            print("{} aruments:".format(len(a) - 1))
            for i in range(len(a) - 1):
                print("{}:".format(i + 1), a[i + 1])
