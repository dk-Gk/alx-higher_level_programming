#!/usr/bin/python3
"""What's my status?"""

if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(r.text))
    print('\t- content:', r.text)
