import requests
import pytest

class TestApiUsers:
    
    
        #Send verification code to email, needs to be put in the verify test with the same email
        def test_sign_up_user(self):
                
                #Arrange
                url = "http://18.202.253.30:8080/auth/sign-up"
                payload = {
                        "username": "9914kach@gmail.com",
                        "password": "Password123!"
                }
                
                #Act
                request = requests.post(url, json=payload)
                
                #Assert
                assert request.status_code == 200, "Status code is not 200"

        def test_verify_user(self):
                
                #Arrange
                url = "http://18.202.253.30:8080/auth/verify"
                payload = {
                        "username": "9914kach@gmail.com",
                        "code": "977793"
                }
                
                #Act
                request = requests.post(url, json=payload)
                
                #Assert
                assert request.status_code == 200, "Status code is not 200"
                
        def test_login_user(self):
                
                #Arrange
                url = "http://18.202.253.30:8080/auth/sign-in"
                payload = {
                        "username": "9914kach@gmail.com",
                        "password": "Password123!"
                }
                
                #Act
                request = requests.post(url, payload)
                
                #Assert
                assert request.status_code == 200, "Status code is not 200"
                
                
        def test_forgot_password(self, username = "9914kach@gmail.com"):
                
                #Arrange
                url = "http://18.202.253.30:8080/auth/forgot-password/" + username
                
                #Act
                request = requests.post(url)
                
                #Assert
                assert request.status_code == 200, "Status code is not 200"
                
        def test_confirm_forgot_password(self):
                
                #Arrange
                
                url = "http://18.202.253.30:8080/auth/confirm-forgot-password"
                payload = {
                        "username": "9914kach@gmail.com",
                        "password": "Password123?",
                        "confirmationCode": "856404"
                }
                
                #Act
                request = requests.post(url, json=payload)
                
                #Assert
                assert request.status_code == 200, "Status code is not 200"