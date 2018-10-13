import getpass
import sys
import telnetlib
import time
#user = input("Enter your telnet username: ")
password = getpass.getpass()


for host in range (200, 204):

    #HOST = "192.168.206." + str(host)
    tn = telnetlib.Telnet("192.168.206.{}".format(host))
    tn.read_until(b"Username: ")
    tn.write(b"jos" + b"\n")

    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('utf-8') + b"\n")

    tn.write(b"sh ip int brie" + b"\n")
    #time.sleep(1)
    #tn.write(b"end\n")
    tn.write(b"exit\n")
    print()
    print()
    #my_text = tn.set_debuglevel(1000)
    my_text = tn.read_all()
    print(my_text)
    tn.close()
