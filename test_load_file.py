import requests
url = "http://127.0.0.1:8000/file"
response = requests.get(url)
with open ("new_file.xlsx", "wb") as file:
    file.write(response.content)