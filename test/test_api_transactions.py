import requests
import pytest

class TestApiTransactions:
    
    def test_transaction_status_code(self, transactionID = "1"):
        
        url = "http://18.202.253.30:8080/transactions/" + transactionID
        assert requests.get(url).status_code == 200, "Status code is not 200"
        
    def test_transaction_by_userId(self):
        
        userId = "1"
        
        url = "http://18.202.253.30:8080/transactions/userTransactions/" + userId
       
        r = requests.get(url)
       
        response = r.json()
       
        for i in response:
            assert i["TransactionID"] == 1, "User ID does not exist"
    
        
        