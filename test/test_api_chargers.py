from urllib import response
import requests
import pytest

class TestApiChargers:

    def test_api_status_code(self):
        r = requests.get("http://18.202.253.30:8080/chargers")
        assert r.status_code ==200, "Status code is not 200"

    def test_api_encoding(self):
        r = requests.get("http://18.202.253.30:8080/")
        assert r.encoding == "utf-8", "Encoding is not utf-8"
    
    def test_chargerid_exists(self, chargerid = "100009"):
        
        url = "http://18.202.253.30:8080/chargers/" + chargerid

        r = requests.get(url)
        
        response_body = r.json()
    
        assert response_body["chargerID"] == 100009, "ChargerID does not exist"
        
    def test_chargerid_exists_status_code(self, chargerid = "100009"):
        
        url = "http://18.202.253.30:8080/chargers/" + chargerid

        r = requests.get(url)
            
        assert r.status_code == 200, "Charger with id: " + chargerid + " does not exist."    
    
    def test_charger_does_not_exist_status_code(self, chargerid="10009"):
        
        url = "http://18.202.253.30:8080/chargers/" + chargerid
            
        r = requests.get(url)
        
        assert r.status_code == 404, "Charger with id: " + chargerid + " exists."    
        
        
    #Function to test if charger is available
    #DOESNT WORK PROPERLY
    def test_charger_status_is_available(self, chargerid = "100009"):
                
        url = "http://18.202.253.30:8080/chargers/" + chargerid
        
        r = requests.get(url)

        try:
            response_body = r.json()
            #Status of the charger
            availability = response_body["status"]
            print(availability)
            #id = 100009, status is "Available"
            #id = 100011, status is "reserved"        
            assert availability == "Available", "Charger is not available"

        except:
            assert r.status_code == 200, "Charger with id: " + chargerid + " does not exist."
        
    def test_charger_serialnmbr(self, serialnmbr = "testnumber15"):
        
        url = "http://18.202.253.30:8080/chargers/serial/" + serialnmbr
        
        r = requests.get(url)
        
        response_body = r.json()
        
        assert response_body["serialNumber"] == serialnmbr, "Serial number does not exist"
        
        