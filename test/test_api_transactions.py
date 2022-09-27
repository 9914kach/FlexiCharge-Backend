import requests
import pytest

class TestApiTransactions:
    
    def test_transaction_status_code(self, transactionID = "1"):
        
        url = "http://18.202.253.30:8080/transactions/" + transactionID
        assert requests.get(url).status_code == 200, "Status code is not 200"
        
        
    #TODO
    #Currently only checks if transactions exists with the userID
    def test_transaction_by_userId(self):
        
        userId = "1"
        
        url = "http://18.202.253.30:8080/transactions/userTransactions/" + userId
       
        r = requests.get(url)
       
        response = r.json()
       
        assert r.status_code == 200, "Status code is not 200"
    
        
        