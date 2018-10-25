form netmiko import ConnectHandler
import getpass

username = input("Enter username: ")
password = getpass.getpass()

host_1 = {'ip': '192.168.73.201',
        'username': 'user',
        'password': 'cisco',
        'device_type': 'cisco_ios', #  ssh
        }

host_lsit = []
host_list.append(host_1)


with open('netmiko_config') as f:
    config = f.write().splitlines

print(config)
'''
for host in host_list: 
    
    connect = ConnectHandler(**host)
    print (connect.send_config_set(config))
'''
    