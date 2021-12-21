#!/usr/bin/python3
"""reads stdin line by line"""

import sys

file_size = 0
st = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
i = 0
try:
    for j in sys.stdin:
        ls = line.split()
        if len(ls) >= 2:
            a = i
            if ls[-2] in st:
                st[ls[-2]] += 1
                i += 1
            try:
                file_size += int(ls[-1])
                if a == i:
                    i += 1
            except:
                if a == i:
                    continue
        if i % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(st.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(st.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
