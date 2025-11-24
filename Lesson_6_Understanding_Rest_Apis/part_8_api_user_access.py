import requests

headers = {
    "Authorization": "Bearer your_token_here"
}

response = requests.get("https://api.example.com/users", headers=headers)

if response.status_code == 200:
    print("Authorized access to users data")
else:
    print("Unauthorized access")
