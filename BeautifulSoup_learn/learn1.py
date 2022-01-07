import urllib.request 
import urllib.parse as parse
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

result = soup.select("h3.h_lst > span.blind")
value = soup.select("span.value")

while True:
    select = int(input("금융번호를 입력하세요(0~11): "))
    
    for i in range(0, 12):
        if i == select:
            print(result[i].string,": ",value[i].string)