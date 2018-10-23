import time
import getpass
from send_command_telnet import send_command_telnet as telnet
# send_command_telnet(host, command, user, password):


try:
    user = input('Enter username: ')
except:
    user = raw_input('Enter username: ')

password = getpass.getpass()



hosts_list = ['192.168.73.200','192.168.73.201']
#hosts_list = ['192.168.73.201']
command_list = ['conf t',
                'ip domain-name cisco.com',
                'crypto key generate rsa',
                'yes',
                '1024'
               ]

for host in hosts_list:
    
    res = telnet(host, command_list, user, password)
    time.sleep(1)
    print(res)

'''
conf t
ip domain-name cisco.com
crypto key generate rsa
1024
'''