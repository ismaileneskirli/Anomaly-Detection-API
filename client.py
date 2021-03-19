#For accessing API.
import  requests
from requests import post, get
from requests.api import put

BASE = "http://localhost:5000/"
dictionary = {1:  10, 2: 11, 3: 9, 4:12, 5:10000 ,6:1, 7:10, 8:12, 9:13}


response = requests.put(BASE, dictionary)
print(response.json())