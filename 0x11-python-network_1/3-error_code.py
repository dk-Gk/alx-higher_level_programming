#!/usr/bin/python3
"""Error code"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
