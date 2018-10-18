import getpass
import sys
import telnetlib
import time

# user = input("Enter your remote account: ")
# password = getpass.getpass()
user = b'jos\n'
password = b'Boroda_11\n'

for i in range (200,202):
    
    HOST = "192.168.73.{}".format(i)
    print(HOST)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    #tn.write(user.encode('utf-8') + b"\n")
    tn.write(user)

    if password:
        tn.read_until(b"Password: ")
        #tn.write(password.encode('utf-8') + b"\n")
        tn.write(password)

    #tn.read_until(b"#")
    tn.write(b"conf t\n")
    #tn.read_until(b"#")
    
    for vlan in range(2,10):

        tn.write(b"vlan " + str(vlan).encode('utf-8') + b"\n")
        tn.write(b"name Vlan_" + str(vlan).encode('utf-8') + b"\n")
    tn.write(b"end")
    tn.write(b"exit")

    #print(HOST)
    time.sleep(1)
    print(tn.read_all())
    tn.close()
    #print(tn.expect('["IOU1(config-vlan)#", "IOU2(config-vlan)#"]', 2))
    print("="*20)
