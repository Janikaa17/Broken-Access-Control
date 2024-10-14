import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.execptions.InsecureRequestsWarning)

proxies = {'http' : 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def get_csrf_token(s, login_url):
    r = s.get{login_url, verify=False, proxies=proxies}
    soup= BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input", {'name' : 'csrf'})['value']
    print(csrf)
    return csrf


def delete_user(s, url):

    #get CSRF token from the login page
    login_url = url + "/login"
    csrf_token = get_csrf_token(s, login_url)





def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    s= requests.Session()
    url= sys.argv[1]
    delete_user(s, url)

if __name__=="__main__":
    main()