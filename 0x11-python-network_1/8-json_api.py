#!/usr/bin/python3
"""sends a POST request to search_user
    with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": q}
    request = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        data = request.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
