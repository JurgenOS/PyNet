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



import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))



Traceback (most recent call last):
  File "send_command_telnet.py", line 41, in <module>
    user = raw_input("Enter your remote account: ")
NameError: name 'raw_input' is not defined




