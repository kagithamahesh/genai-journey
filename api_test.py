import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

data = response.json()

print("Titile:",data["title"])
print("Body:", data["body"])