import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        users = response.json()

        print("ID   Name                 Email")
        print("-" * 40)

        for user in users[:5]:
            print(f"{user['id']}   {user['name']}   {user['email']}")

    elif response.status_code == 404:
        print("Error: Data not found")

    else:
        print("Error:", response.status_code)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")