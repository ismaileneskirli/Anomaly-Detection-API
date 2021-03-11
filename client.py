#For accessing API.
import  requests
from requests import post, get
from requests.api import put


dictionary = {1:  10, 2: 11, 3: 9, 4:12, 5:55}
#print(post('http://localhost:5000/sampledict/?number=10').json())
#print(get('http://localhost:5000/dictionary/', data =dictionary).json())
print(post('http://localhost:5000/dictionary', data =dictionary).json())