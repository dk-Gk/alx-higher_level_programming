#!/usr/bin/python3
"""POST an email"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse
    d = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    with urllib.request.urlopen(url=sys.argv[1], data=d) as response:
        print(response.read().decode('UTF-8'))
