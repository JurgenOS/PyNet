import getpass
import telnetlib
import sys

user = input("Enter your remote account: ")
password = getpass.getpass()

for host in range (200, 203):

    tn = telnetlib.Telnet("192.168.206.{}".format(host))
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"sh ip int brie\n")
    
    print(tn.read_all().decode('ascii'))
