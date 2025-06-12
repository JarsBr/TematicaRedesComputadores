import requests
from bs4 import BeautifulSoup

### ----- HTTPS ----- ###
### filtro wireshark: ip.addr == 10.44.132.11 && ip.addr == 23.202.27.172 && tls

url_https = "https://www.ibm.com/br-pt/topics/networking"
response_https = requests.get(url_https)

if response_https.status_code == 200:
    print("Page fetched successfuly")
else:
    print("Error")

soup_https = BeautifulSoup(response_https.content, "html.parser")


title = soup_https.find("h1").text
print(title.replace("\n", ""))

description = soup_https.find("div", id="rich-text-a486a0a632").text
print(description)

with open("WebScraping/HTTPs/site_https.txt", "w", encoding="utf-8") as f:
    f.write(f"# {title}\n\n")
    f.write(f"{description}\n")