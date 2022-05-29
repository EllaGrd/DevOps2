from datetime import datetime
import requests

print(datetime.now())

response = requests.get("https://api.github.com/users/avielb/repos")

if response.status_code == 200:
    print("github is ok")
print(datetime.now())

def url_caller(url):

 response = requests.get("url")

if response.status_code == 200:
    print(f"{url} is ok")

for url in ["https://github.com",
            "https://google.com]",
             "https://david.com"]:
    url_caller(url)



