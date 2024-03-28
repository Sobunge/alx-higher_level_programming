#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        print("\t- body response:")
        print("\t\t- type: {}".format(type(html)))
        print("\t\t- content: {}".format(html))
except urllib.error.URLError as e:
    print("Error fetching URL:", e)

