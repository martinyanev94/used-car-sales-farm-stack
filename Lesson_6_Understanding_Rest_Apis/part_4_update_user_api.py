import requests

updated_user = {
    "name": "John Doe",
    "email": "john.new@example.com"
}

response = requests.put("https://api.example.com/users/1", json=updated_user)

if response.status_code == 200:
    print("User updated successfully")
else:
    print("Failed to update user")
