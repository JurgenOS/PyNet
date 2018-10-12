import getpass
import telnetlib
import sys
import time

#user = input("Enter your remote account: ")
user = "jos"
#password = getpass.getpass()
password = "Boroda_11"

for host in range (200, 203):

    tn = telnetlib.Telnet("192.168.206.{}".format(host))
    time.sleep(2)
    tn.read_until(b"Username: ")
    time.sleep(2)
    tn.write(b"jos\n")

    if password:
        time.sleep(2)
        tn.read_until(b"Password: ")
        tn.write(b"Boroda_11\n")

    tn.read_very_eager()
    time.sleep(2)
    tn.expect(b".*[>#]")
    tn.write(b"\n")
    tn.write(b"sh ip int brie\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_very_eager())
