import os
from datetime import datetime
import requests
import json 
import time as std_time

cwd = os.getcwd()
os.chdir(r"D:\Pruebas_tecnicas\lumu\lumu_prueba_tecnica")


url = "https://api.lumu.io/collectors/5ab55d08-ae72-4017-a41c-d9d735360288/dns/queries?key=d39a0f19-7278-4a64-a255-b7646d1ace80"

headers = {
    "Content-Type": "application/json"
}

json_body = []
ip_count= {}
name_count = {}
 
with open("queries") as my_file:
    lines = my_file.readlines()
    # for item,value in enumerate(lines[0].split()):
    #         print(item,value)
      
    for line in lines:
        name=line.split()[9]
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
        client_ip= line.split()[6].split("#")[0]

        ##this is for the count of name and ips. 
        ip_count[client_ip] = ip_count.get(client_ip, 0) + 1
        name_count[name] = name_count.get(name, 0) + 1

        ### Body dictionary
        body=[{ "timestamp": "",
        "name": "",
        "client_ip": ""}]
        body[0]["name"]=name
        body[0]["client_ip"]=client_ip
        body[0]["timestamp"]=timestamp
        json_string=json.dumps(body)
        json_body.append(json_string)



# Sort the ip_count dictionary by repetitions in descending order
sorted_ip_count = dict(sorted(ip_count.items(), key=lambda x: x[1], reverse=True))

# Calculate the total count of client_ips
total_count = sum(sorted_ip_count.values())

# Create and print the table for Clients IPs Rank

print(f"\nTotal records {len(json_body)}\n")
print(f"Clients IPs Rank")

print("-" * 50)
for ip, count in sorted_ip_count.items():
    percentage = (count / total_count) * 100
    print(f"{ip.ljust(20)}{str(count).rjust(15)}{f'{percentage:.2f}%'.rjust(15)}")


# Sort the name_count dictionary by repetitions in descending order
sorted_name_count = dict(sorted(name_count.items(), key=lambda x: x[1], reverse=True))

# Calculate the total count of names
total_count = sum(sorted_name_count.values())

# Create and print the table
print(f"\nHost Rank")


print("-" * 120)
for name, count in sorted_name_count.items():
    percentage = (count / total_count) * 100
    print(f"{name.ljust(90)}{str(count).rjust(15)}{f'{percentage:.2f}%'.rjust(15)}")

### make the requests
for i,dictionary in enumerate(json_body):
    
    start_time = std_time.time()
    print(i)
    response = requests.post(url, json=json.loads(dictionary), headers=headers)
    end_time = std_time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    print(response)

     




