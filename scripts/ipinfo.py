
"""
This Program help you to find origin country of a website
and also provides you detail information of whois
"""

import socket
import requests
import os

host = input("Please Enter a website to find it's origin: ")
addra = socket.gethostbyname(host)
url = 'http://ipinfo.io/{}'.format(addra)
country = requests.get(url, verify=False)
print("{} hosted country is: ".format(host) + country.json()['country'])
print('#' * 50)
print("{} whois information".format(host))
print('*' * 50)
sys = os.system('whois {}'.format(addra))
