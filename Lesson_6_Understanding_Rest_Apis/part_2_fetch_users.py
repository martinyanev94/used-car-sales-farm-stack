import requests

response = requests.get("https://api.example.com/users")
if response.status_code == 200:
    users = response.json()
    print(users)
else:
    print("Failed to retrieve users")
