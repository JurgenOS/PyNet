import getpass
import sockets
import send_command_ssh
import send_command_telnet


try:
    username = input("Enter the username: ")
except:
    username = raw_input("Enter the username: ")

password = getpass.getpass()


command = ['show run']
hosts = ['192.168.73.200', '192.168.73.201']

with open('new_configs.txt', 'w') as file:

    for host in hosts:

        print('Getting config from {}'.format(host))
        node = sockets.socket_checker(host)
        
        if node['SSH']:
            conf = send_command_ssh.send_command_ssh(host, username, password, command)
        else:
            conf = send_command_telnet.send_command_telnet(host, username, password, command)

        file.write(conf)
