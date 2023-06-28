import requests
from decouple import config

# Define the URL
url = 'http://127.0.0.1:8000/todo/api/todos/'

# Define the headers for the request
headers = {f'Authorization': f'Token {config("TOKEN")}',}

# Make the GET request
response = requests.get(url, headers=headers, verify=False)

# Print the status code and the content of the response
print(headers)
print("Response status code:", response.status_code)
try:
    print("Response content:", response.json())
except Exception as e:
    print(e)