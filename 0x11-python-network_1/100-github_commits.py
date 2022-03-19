#!/usr/bin/python3
"""Time for an interview!"""

if __name__ == '__main__':
    import requests
    import sys


    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    params = {
        'per_page': 10,
    }

    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]),
                       headers=headers, params=params)
    jr = res.json()
    for c in jr:
        print(c['sha'] + ':', c['commit']['author']['name'])
