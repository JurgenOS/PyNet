import getpass
import sys
import telnetlib

#user = input("Enter your remote account: ")
#password = getpass.getpass()
password = "Boroda_11"

for i in range (200,201):

    HOST = "192.168.206.{}".format(i)
    print(HOST)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(b"jos" + b"\n")


    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('utf-8') + b"\n")

    tn.write(b"conf t\n")
    #tn.read_until(b"#")
    tn.read_until(b"S1(config)#", timeout = 5)
    
    for vlan in range(2,10):
        command = "vlan " + str(vlan) + "\n"
        #print(command)
        tn.write(command.encode("utf-8"))
        #print(tn.read_until(b"#"))
        command = "name VLAN" + str(vlan) + "\n"
        #print(command)
        tn.write(command.encode('utf-8'))
        #print(tn.read_until(b"#"))

        tn.write(b"exit\n")
    tn.write(b"end\n")
    run = tn.read_until(b"#", timeout = 5)
    print(run)
    print("="*20)
    tn.close()