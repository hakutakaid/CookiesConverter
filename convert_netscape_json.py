import json

def convert_netscape_to_json(file_path):
    cookies = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith('#') or not line.strip():
            continue
        
        parts = line.strip().split('\t')
        if len(parts) < 7:
            continue

        domain, flag, path, secure, expiry, name, value = parts

        expiry = float(expiry)
        if expiry < 1000000000:
            expiry += 2147483648

        cookie = {
            "domain": domain,
            "expirationDate": expiry,
            "hostOnly": not flag.upper() == 'TRUE',
            "httpOnly": not secure.upper() == 'TRUE',
            "name": name,
            "path": path,
            "sameSite": "no_restriction",
            "secure": secure.upper() == 'TRUE',
            "session": False,
            "storeId": "0",
            "value": value
        }

        cookies.append(cookie)

    return cookies

file_path = 'cookies.txt'
cookies_json = convert_netscape_to_json(file_path)

output_file = 'cookies.json'
with open(output_file, 'w') as json_file:
    json.dump(cookies_json, json_file, indent=2)

print(f'Cookies have been converted to JSON and saved to {output_file}')
