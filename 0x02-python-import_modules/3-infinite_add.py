#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = sys.argv
    sum = 0
    if (len(a) == 2):
        print("{}".format(int(a[1])))
    else:
        if (len(a) == 1):
            print("{}".format(len(a) - 1))
        else:
            for i in range(len(a) - 1):
                sum = sum + int(a[i + 1])
                print("{}".format(sum))
