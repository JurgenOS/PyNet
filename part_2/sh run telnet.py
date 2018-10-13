import getpass
import sys
import telnetlib
import time
import re

user = input("Enter your telnet username: ")
password = getpass.getpass()
password = "Boroda_11"

for host in range (200, 201):

    #HOST = "192.168.206." + str(host)
    tn = telnetlib.Telnet("192.168.206.{}".format(host))
    tn.read_until(b"Username: ")
    tn.write(user.encode('utf-8') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('utf-8') + b"\n")
    print("Let's go!!")

    pattern = b'\S+?[#>]'
    bin_pattern = re.compile(pattern)


    tn.write(b"terminal length 0\n")
    tn.expect([bin_pattern], 2)

    tn.write(b"show run\n")
    tn.expect([bin_pattern], 2)

    time.sleep(10)
    tn.write(b"exit\n")
    
    regex_idx, match, output = tn.expect([bin_pattern], 2)
    print(output)



    #run = tn.read_all()
    #time.sleep(5)
    #run = tn.read_very_eager()
    #print(run)

    #my_text = tn.read_all()
    #print(my_text)
    tn.close()