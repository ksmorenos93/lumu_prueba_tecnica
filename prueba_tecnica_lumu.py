import http.client
import os


cwd = os.getcwd()
print(cwd)

#  body={{ "timestamp": "",
# #         name": "www.example.com",
# #         "client_ip": "192.168.0.103",
# #         "client_name": "MACHINE-0987",
# #         "type": "A"}}

with open("queries") as my_file:
    lines = my_file.readlines()
    print(lines[1])
    for item,value in enumerate(lines[0].split()):
            print(item,value)
    for line in lines[0:2]:
        try:
            #print(line.split()[9])
            name=line.split()[9]
            print(f"name: {name}")
        except:
             pass
        fecha=line.split()[0]
        time= line.split()[1] 
        timestamp=f"timestamp:{fecha}T{time}Z"
        print(timestamp)
        client_ip= line.split()[6]
        print(f"client_ip: {client_ip}"+"/n")

       

        

7-Jul-2022 16:34:13.003 queries: info: client @0x55adcc672cc0 45.231.61.2#80 (pizzaseo.com): query: pizzaseo.com IN ANY +E(0) (172.20.101.44)

Date: 18-May-2021,
time: 16:34:13.003, 
hexadecimal_representation_: 0x55adcc672cc0,
ip: 45.231.61.2
host_queried: pizzaseo.com, 
class_of_query: IN,
type_of_query: A.


[ { "timestamp": "2021-01-06T14:37:02.228Z", "name": "www.example.com", "client_ip": "192.168.0.103", "client_name": "MACHINE-0987", "type": "A" } ]


    
host = 'https://api.lumu.io'

lumu_client_key= d39a0f19-7278-4a64-a255-b7646d1ace80
collector_id=5ab55d08-ae72-4017-a41c-d9d735360288

headers = {"Content-type": "application/json"}

connection = http.client.HTTPConnection(host)

## Body parameters
[ { "id": 69, "timestamp": "2021-01-05T14:37:02.228Z", "client_ip": "192.168.0.103", "client_name": "User9800", "op_code": "QUERY", "response_code": "NOERROR",
    "question": { "type": "A", "name": "www.example.com", "class": "IN" }, "flags": { "authoritative": false, "recursion_available": true,
 "truncated_response": false, "checking_disabled": false, "recursion_desired": true, "authentic_data": false }, 
 "answers": [ { "name": "www.example.com", "type": "A", "class": "IN", "ttl": 2549, "data": "69.172.201.153" } ] } ]