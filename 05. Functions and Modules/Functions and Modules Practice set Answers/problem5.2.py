import requests # pip install requests

a = requests.get("https://api.github.com/")
print(a.json())