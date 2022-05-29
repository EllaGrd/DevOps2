import requests
response = requests.get("https://api.github.com/users/avielb/repos")

result = response.json()
for repo in result:
    print(repo["name"])

