import requests
from bs4 import BeautifulSoup
import sys
info = {
    "version":"v1",
    "creator":"xwbash"
}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
cookies = {'antibot': "0ffb515c2bb41440c468d6fee1453ca8"}
def proxy_s():
    Intro()
    r = requests.get("https://free-proxy-list.net/",headers = headers, cookies=cookies)
    source = BeautifulSoup(r.content, "html.parser")
    sources = source.find("tbody")
    sources = sources.findAll("td")
    sources=[x.text.strip() for x in sources]
    first = 0
    second = 2
    file_proxy = open("proxy.txt","a")
    proxy_text = []
    while(first<=160):
        text = sources[first:second]
        text =str(text).strip('[]').replace(" ","").replace("'","").replace(",",":")
        first += 8
        second += 8
        file_proxy.write(text+"\n")
    file_proxy.close()
def UserAgent():
    file_useragent = open("useragent.txt", "a")
    r = requests.get("https://generate-name.net/user-agent")
    source = BeautifulSoup(r.content, "lxml")
    source = source.findAll("td", attrs={"class":"name"})
    for i in source:
        file_useragent.write(i.text+"\n")
def Intro():
    print("""
    Creator; %s 
    Version; %s"""%(info["creator"],info["version"]))
for i in sys.argv:
    if(i == "-proxy" or i == "--proxy"):
        proxy_s()
    elif(i == "-ua" or i == "--ua"):
        UserAgent()
    elif(i == "-help" or i == "--help"):
        print("""
        
        Usage[!]; delta.py -proxy or --proxy, delta.py -ua or --ua
        
        """)