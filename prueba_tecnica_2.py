
import os
from datetime import datetime
import requests
import json 

cwd = os.getcwd()
os.chdir(r"D:\Pruebas_tecnicas\lumu\lumu_prueba_tecnica")
print(cwd)

url = "https://api.lumu.io/collectors/5ab55d08-ae72-4017-a41c-d9d735360288/dns/queries?key=d39a0f19-7278-4a64-a255-b7646d1ace80"

headers = {
    "Content-Type": "application/json"
}

json_body = []
 
with open("queries") as my_file:
    lines = my_file.readlines()
    print(lines[1])
    # for item,value in enumerate(lines[0].split()):
    #         print(item,value)

    print("")        
    for line in lines[0:100]:
        name=line.split()[9]
        print(f"name: {name}")
        fecha=line.split()[0]
        time= line.split()[1] 
        # Convert the date_str to a datetime object
        date_datetime = datetime.strptime(fecha, '%d-%b-%Y')

        # Combine date_datetime with the time_str to create a new datetime object
        combined_datetime = date_datetime.replace(hour=int(time[:2]),
                                                minute=int(time[3:5]),
                                                second=int(time[6:8]),
                                                microsecond=int(time[9:]) * 1000)

        # Format the combined_datetime as a string in the desired format
        timestamp = combined_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

        
        print(f"timestamp:{timestamp}")
        client_ip= line.split()[6].split("#")[0]
        ### Body dictionary
        body=[{ "timestamp": "",
        "name": "",
        "client_ip": ""}]
        print(f"client_ip: {client_ip}\n")
        body[0]["name"]=name
        body[0]["client_ip"]=client_ip
        body[0]["timestamp"]=timestamp
        json_string=json.dumps(body)
        json_body.append(json_string)

print(json_body)

for i in json_body:
    print(i)
    print("")
    response = requests.post(url, json=json.loads(i), headers=headers)
    print(response)
    print("kevin",response.status_code)
    print("text:",response.headers)
    print("")
     





# 7-Jul-2022 16:34:13.003 queries: info: client @0x55adcc672cc0 45.231.61.2#80 (pizzaseo.com): query: pizzaseo.com IN ANY +E(0) (172.20.101.44)

# Date: 18-May-2021,
# time: 16:34:13.003, 
# hexadecimal_representation_: 0x55adcc672cc0,
# ip: 45.231.61.2
# host_queried: pizzaseo.com, 
# class_of_query: IN,
# type_of_query: A.


# [ { "timestamp": "2021-01-06T14:37:02.228Z", "name": "www.example.com", "client_ip": "192.168.0.103", "client_name": "MACHINE-0987", "type": "A" } ]


    
# host = 'https://api.lumu.io'

# lumu_client_key= d39a0f19-7278-4a64-a255-b7646d1ace80
# collector_id=5ab55d08-ae72-4017-a41c-d9d735360288

# headers = {"Content-type": "application/json"}

# connection = http.client.HTTPConnection(host)

# ## Body parameters
# [ { "id": 69, "timestamp": "2021-01-05T14:37:02.228Z", "client_ip": "192.168.0.103", "client_name": "User9800", "op_code": "QUERY", "response_code": "NOERROR",
#     "question": { "type": "A", "name": "www.example.com", "class": "IN" }, "flags": { "authoritative": false, "recursion_available": true,
#  "truncated_response": false, "checking_disabled": false, "recursion_desired": true, "authentic_data": false }, 
#  "answers": [ { "name": "www.example.com", "type": "A", "class": "IN", "ttl": 2549, "data": "69.172.201.153" } ] } ]