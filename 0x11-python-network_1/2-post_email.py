#!/usr/bin/python3
"""POST an email"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    d = urllib.parse.urlencode({'email': argv[2]}).encode('ascii')
    with urllib.request.urlopen(url=argv[1], data=d) as response:
        print(response.read().decode('UTF-8'))
