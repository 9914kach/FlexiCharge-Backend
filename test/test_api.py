from urllib import response
import requests
import pytest

class TestApi:
    
    
    def test_api_status_code(self):
        r = requests.get("http://18.202.253.30:8080/")
        assert r.status_code ==200, "Status code is not 200"

    def test_api_encoding(self):
        r = requests.get("http://18.202.253.30:8080/")
        assert r.encoding == "utf-8", "Encoding is not utf-8"
    
    def test_chargerid_exists(self, expected_chargerid = 100009):
        
        r = requests.get("http://18.202.253.30:8080/chargers")
        
        response_body = r.json()
        index = 0
        max_length = len(response_body)
        for i in response_body:
            if i["chargerID"] == expected_chargerid:
                break
            if index < max_length - 1:
                index += 1
        
        assert response_body[index]["chargerID"] == expected_chargerid, "ChargerID does not exist"
            
    def test_charger_is_available(self, expected_chargerid = 100009):
        
        r = requests.get("http://18.202.253.30:8080/chargers")

        response_body = r.json()
        
        charger = response_body[0]["chargerID"]
        
        
        