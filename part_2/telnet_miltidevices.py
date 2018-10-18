import getpass
import sys
import telnetlib
import time

#HOST = "192.168.73.200"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()
host_list = ['192.168.73.200', '192.168.73.210']

for host in host_list:

    tn = telnetlib.Telnet(host)
    
    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    
    tn.write("conf t\n")

    for i in range(10):
        tn.write("interface loopback {}\n".format(i))
        tn.write("description LOOP_{}\n".format(i))
        tn.write("\n")
        time.sleep(1)
    tn.write("end\n")    
    tn.write("\n")
    time.sleep(2)
    tn.write("exit\n")
    print tn.read_all()



