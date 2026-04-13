import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json()

print("Titile:",len(data["title"]))
print("Body:", len(data["body"].split(" ")))