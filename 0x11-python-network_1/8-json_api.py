#!/usr/bin/python3
"""Search API"""

if __name__ == "__main__":
    import sys
    import requests

    val = ""
    if len(argv) == 2:
        arg = argv[1]
        try:
            res = requests.post('http://0.0.0.0:5000/search_user', data={'q': arg})
            js = r.json()
            if js:
                print('[{}] {}'.format(js.get('id'), js.get('name')))
            else:
                print('No result')
        except ValueError:
            print('Not a valid JSON')
