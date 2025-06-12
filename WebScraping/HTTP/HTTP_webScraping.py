import requests
from bs4 import BeautifulSoup

### ----- HTTP ----- ###
### filtro wireshark: ip.addr == 10.44.132.11 && ip.addr == 146.190.62.39

url_http = "http://httpforever.com" 
response_http = requests.get(url_http)

if response_http.status_code == 200:
    print("Page fetched successfuly")
else:
    print("Error")

soup_http = BeautifulSoup(response_http.content, "html.parser")


title = soup_http.find("h2").text
print(title)

description = soup_http.find("div", class_="wrapper style1").text
print(description)