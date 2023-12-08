# PingDelayStudy
# Author: Sarah Kugelmas

import os

with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    # ping for each ip in the file

for ip in park:
    response = os.popen(f"ping -c 5 -i 1 {ip} ").read()
    
    #saving some ping output details to output file
    if ("Request timed out." or "unreachable") in response:
        print(response)
        f = open("info_output.txt","a")
        f.write(str(ip) + ' link is down'+'\n')
        f.close() 
    else:
        print(response)
        f = open("info_output.txt","a")  
        f.write(response +'\n')
        f.close() 

# print output file to screen
#with open("info_output.txt") as file:
 #   output = file.read()
  #  f.close()
