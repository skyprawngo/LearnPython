import pandas as pd

url ='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8%EC%A1%B0%ED%9A%8C'

tables = pd.read_html(url)
print(tables)
print(tables[0])