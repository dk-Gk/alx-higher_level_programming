#!/usr/bin/python3
"""Response header"""

if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.info()['X-Request-Id'])
