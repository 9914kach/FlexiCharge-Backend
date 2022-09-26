import requests
import pytest
    
def test():
    chargerid= "100009"
    url = "http://18.202.253.30:8080/chargers/" + chargerid

    r = requests.get(url)
    
    response_body = r.json()
    
    print(response_body["status"])  

test()