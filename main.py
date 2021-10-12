import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
from multiprocessing import Process

def getPage(domain_name):
    url = "https://www.registry.in/domain-search"

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Origin"] = "null"
    headers["Connection"] = "keep-alive"
    headers["Upgrade-Insecure-Requests"] = "1"

    data = f"domainUniquelang=english&domain_name={domain_name}&tld=in&domain=&referer=https%3A%2F%2Fwww.registry.in%2Fdomain-search&is_domain_available=&op=SEARCH"
    resp = requests.post(url, headers=headers, data=data)

    return(resp.text)

def pageParser(domain_name):
    soup = BeautifulSoup(getPage(domain_name), 'html.parser')
    print(domain_name + (" is not available" if soup.select(".text-center-align") else " is available"))
    

while(True):
    domain_name = input("Type the name without .in: ")
    if(domain_name == "0"):
        break

    checker = Process(target=pageParser, args=(domain_name,))
    checker.start()
    
checker.join()
