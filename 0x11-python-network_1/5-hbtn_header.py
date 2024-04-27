#!/usr/bin/python3
"""sends request to url and
    display X-Request-Id header value
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    request_id = response.headers.get('X-Request-Id')
    print(request_id)
