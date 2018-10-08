import getpass
import sys
import telnetlib

user = input("Enter your remote account: ")
password = getpass.getpass()


for i in range (200,203):
    
    HOST = "192.168.206.{}".format(i)
    print(HOST)
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")

    for vlan in range(2,10):

        tn.write("vlan {}\n".format(vlan))
        tn.write("name Vlan_{}".format(vlan))
    print(HOST)
    print(tn.read_all())
    print("="*20)
