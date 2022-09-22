import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
url = "https://www.google.com"
res = requests.get(url,headers = headers)
res.encoding = 'utf-8'
if res.status_code == 200:
    # print(res.text)
    soup = BeautifulSoup(res.text,'html.parser')
    a = soup.select("input.gNO89b")
    b = soup.select("input.gLFyf.gsfi")
    print(a)
    print(b)