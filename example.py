import requests
import pytest
    
def test():
    
    #Arrange
    url = "http://18.202.253.30:8080/chargers"
    payload = {
            "chargerPointNumber": 23,
            "location": [57.777714, 14.16301],
            "serialNumber": "android"
            }
    headers = {"Authorization": ""}
        
    #Act
    request = requests.post(url, json=payload, headers=headers)
    
    #Asserts
    print(request.status_code)
    assert request.status_code == 200, "Status code is not 200"    
    
    


    
    
    
test()