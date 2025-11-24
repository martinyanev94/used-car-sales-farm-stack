import requests

response = requests.delete("https://api.example.com/users/1")

if response.status_code == 204:
    print("User deleted successfully")
else:
    print("Failed to delete user")
