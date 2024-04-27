#!/usr/bin/python3
"""send a request to a URL and
    display value of X-Request_Id
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
