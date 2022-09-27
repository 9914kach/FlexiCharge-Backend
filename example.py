import requests
import pytest
    
def test(foo = "8"):
    url = "http://18.202.253.30:8080/reservations" + foo
    
    print(requests.get(url).status_code)
    
   
    


    
    
    
test()