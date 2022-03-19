#!/usr/bin/python3
'''task 0 script'''


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', html.decode('UTF-8'))
