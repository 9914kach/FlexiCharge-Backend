import requests
import pytest
    
def test(userid = "1"):
    url = "http://18.202.253.30:8080/transactions//userTransactions/" + userid


    r = requests.get(url)
 
    response = r.json()
    
    
    for i in response:
        print(i["transactionID"])
test()