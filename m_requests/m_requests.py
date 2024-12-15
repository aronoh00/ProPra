import requests
from bs4 import BeautifulSoup
import sys
import json

def do_get(url: str, searchingstring: str):
    r = requests.get(url)
    r.encoding = 'utf-8'


    print("Status:", r.status_code)

    number_of_characters = len(r.text)
    print(f"recived {number_of_characters} characters for {url}")

    print(f"Encoding: {r.encoding}")

    print("Headers:")
    for key, value in r.headers.items(): 
        if not key.lower().startswith('x-'):
            print(f"    {key}: {value}")

    soup = BeautifulSoup(r.text, 'html.parser')
    plain_text = soup.get_text()

    position = plain_text.find(searchingstring)
    if position != -1:
        snippet = plain_text[position:position + 250]
        print(f"Snippet starting at position {position}")
        print(snippet)
    else:
        print("((not found))")

def do_post(url: str, jsontext: str):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=json.loads(jsontext))

    print(f"HTTP Status: {response.status_code}")

    formatted_json = json.dumps(response.json(), indent=4)
    print("Antwort im JSON-Format:")
    print(formatted_json)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python m_requests.py <method> <url> [<json-text> or <searchstring>]")
        sys.exit(1)
    
    method = sys.argv[1]
    if method == "do_get" and len(sys.argv) == 4:
        _, _, url, searchstring = sys.argv
        do_get(url, searchstring)
    elif method == "do_post" and len(sys.argv) == 4:
        _, _, url, jsontext = sys.argv
        do_post(url, jsontext)
    else:
        print("Invalid arguments or method. Usage: python m_requests.py do_get <url> <searchstring> OR do_post <url> <json-text>")