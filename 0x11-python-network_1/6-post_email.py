#!/usr/bin/python3
"""POST an email"""

if __name__ == "__main__":
    import sys
    import requests

    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
