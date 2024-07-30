import json
import time

with open('cookie.json', 'r') as file:
    data = json.load(file)

cookies = data.get('cookies', [])

netscape_cookies = []

for cookie in cookies:
    domain = cookie.get('domain', '')
    path = cookie.get('path', '')
    secure = 'TRUE' if cookie.get('secure', False) else 'FALSE'
    expiration = int(cookie.get('expirationDate', 0))
    name = cookie.get('name', '')
    value = cookie.get('value', '')
    netscape_cookies.append(f"{domain}\tTRUE\t{path}\t{secure}\t{expiration}\t{name}\t{value}")

with open('cookies_netscape.txt', 'w') as file:
    file.write("# Netscape HTTP Cookie File\n")
    file.write("# https://curl.haxx.se/rfc/cookie_spec.html\n")
    file.write("# This is a generated file! Do not edit.\n")
    file.write("\n")
    file.write("\n".join(netscape_cookies))

print("Conversion complete. Check cookies_netscape.txt for the results.")