import requests
import pytest
    
def test():
    
    #Arrange
    url = "http://18.202.253.30:8080/transactions"
    payload =   {
                "userID": "10",
                "chargerID": 100009,
                "isKlarnaPayment": True,
                "pricePerKwh": "333"
                }

        
    #Act
    request = requests.post(url, json=payload)
    
    #Asserts
    print(request.status_code)
    assert request.status_code == 200, "Status code is not 200"    
    
    
def test_signup():
                #Arrange
                url = "http://18.202.253.30:8080/auth/sign-up"
                payload = {
                        "username": "testuser1@email.com",
                        "password": "Password123!"
                }
                
                #Act
                request = requests.post(url, json=payload)
                
                #Assert
                assert request.status_code == 200, "Status code is not 200"
    
def test_login():
    


    
 
test_signup()