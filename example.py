import requests

url = "http://18.202.253.30:8080/chargers"

r = requests.get(url)

content = r.headers["Content-Type"]

response_body = r.json()

testID = 100009

for i in response_body:
    print(i)

    
print(len(response_body))