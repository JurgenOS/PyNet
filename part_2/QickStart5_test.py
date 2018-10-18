import getpass
import sys
import telnetlib
import time

# user = input("Enter your remote account: ")
# password = getpass.getpass()
user = b'jos\n'
password = b'Boroda_11\n'

for i in range (200,201):
    
    HOST = "192.168.73.{}".format(i)
    print(HOST)
    with telnetlib.Telnet(HOST) as tn:

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

            command = "interface loop {}\n".format(vlan)
            tn.write(command.encode('utf-8'))
            command = "description loop {}\n".format(vlan) 
            tn.write(command.encode('utf-8'))
            print(tn.read_until(b'#'))
            time.sleep(1)

        tn.write(b"end")
        tn.write(b"exit")

        #print("slept 10 sec")
        #time.sleep(10)
        #print("woke up")

        print(tn.read_all())
        #print(tn.read_until(b'#'))
        #print(tn.read_until(b'#'))
        #print(tn.read_until(b'#'))
        #print(tn.read_until(b'#'))
        print("="*20)
