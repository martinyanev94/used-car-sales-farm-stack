import requests

new_user = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

response = requests.post("https://api.example.com/users", json=new_user)

if response.status_code == 201:
    print("User created successfully")
else:
    print("Failed to create user")
