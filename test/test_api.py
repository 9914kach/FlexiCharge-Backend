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
    
    def test_chargerid_exists(self, chargerid = "100009"):
        
        url = "http://18.202.253.30:8080/chargers/" + chargerid

        r = requests.get(url)
        
        response_body = r.json()
    
        assert response_body["chargerID"] == 100009, "ChargerID does not exist"
            
    def test_charger_status_is_available(self, chargerid = "100009"):
                
        url = "http://18.202.253.30:8080/chargers/" + chargerid
        
        r = requests.get(url)

        response_body = r.json()
        
        assert response_body["status"] == "Available", "Charger is not available"
    
    def test_charger_serialnmbr(self, serialnmbr = "testnumber15"):
        
        url = "http://18.202.253.30:8080/chargers/serial/" + serialnmbr
        
        r = requests.get(url)
        
        response_body = r.json()
        
        assert response_body["serialNumber"] == serialnmbr, "Serial number does not exist"
        
        