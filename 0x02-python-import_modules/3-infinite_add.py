#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1
    sum = 0
    for i in range(a):
        sum = sum + int(a[i + 1])
    print("{}".format(sum))
