import requests
from bs4 import BeautifulSoup

def getRequest(url:str):
    try:
        return requests.get(url)
    except Exception:
        pass

req = getRequest('http://ip/vulnerabilities/xss_r/')
parsed_html = BeautifulSoup(req.content, features="html5lib")

forms = parsed_html.findAll("form")

for form in forms:
    action = form.get("action")
    print(action)
    method = form.get('method')
    print(method)
    
    input_form = form.findAll("input")

    for input in input_form:
        print(input.get("name"))
    
    