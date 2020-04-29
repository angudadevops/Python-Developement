#! /Users/aguda/opt/anaconda3/bin/python3

import sys,os,json,requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Function to get UUID and Serial Number of a Server
def res(url,user,passw):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    a = requests.get(url,verify=False,auth=(user, passw))
    return '{} Server UUID is: '.format(host) + a.json()['UUID']+"\n"+'{} Server Serial Number is: '.format(host) + a.json()['SerialNumber']

# Input file with read line by line
file =  sys.argv[1]
f = open(file,'r')
lines = f.readlines()

# Itterate the each host to get the RedFish Details
for item in lines:
    # Split based on ":" from file 
    ip = item.strip().split(':')
    host = ip[0]
    print('\n' + '*' * 70)
    # method to validate whether the server is valid for RedFish API
    try:
        url = "https://{}/redfish/v1/".format(host)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url, verify=False,timeout=3)
        # method to get valid RedFish Server details with help of res function
        try:
            oe = response.json()['Oem']
            #Itterate the OEM Patners to get the server details 
            for item in oe:
                if item == 'Dell':
                    dellurl = "https://{}/redfish/v1/Systems/System.Embedded.1".format(host)
                    print("{} Server Service Tag is: ".format(host) + oe['Dell']['ServiceTag'])
                    print(res(dellurl,ip[1],ip[2]))
                elif item == 'Ami':
                    amiurl = "https://{}/redfish/v1/Systems/Self".format(host)
                    print(res(amiurl,ip[1],ip[2]))
                elif item == 'Hp':
                    hpurl = "https://{}/redfish/v1/Systems/1/".format(host)
                    print(res(hpurl,ip[1],ip[2]))
                else:
                    smurl = "https://{}/redfish/v1/Systems/1".format(host)
                    print(res(hpurl,ip[1],ip[2]))
        except Exception as e:
            if 'Oem' in str(e):
                atosurl = "https://{}/redfish/v1".format(host)
                atos = requests.get(atosurl,verify=False)
                print('Atos Server {} UUI is: '.format(host) + atos.json()['UUID'])
    except:
        print('{} Server is not for RedFish API'.format(host))
