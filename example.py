import requests
import pytest
    
def test():
    chargerid= "100011"
    url = "http://18.202.253.30:8080/chargers/" + chargerid
        
    r = requests.get(url)
 
    response = r.json()
    
    foo = response["status"]

    print(foo)

    assert foo == "Available", "Charger is not available"
test()