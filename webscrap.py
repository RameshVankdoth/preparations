import requests
from bs4 import BeautifulSoup

# url = "https://www.w3schools.com/"

# data = requests.get(url)
# soap = BeautifulSoup(data.content, "html.parser")
# print(soap)
# with open("w3school.html", "w", encoding="UTF-8") as f:
#     f.write(str(soap))

url = "https://api64.ipify.org?format=json"
data = requests.get(url)
print(data.json())

# Update
