import paramiko
import getpass
import sys
import time

def send_command_ssh(host, user, pswd, command):
    #host - the ip address of the host in str format, e.g.'1.1.1.1'
    #command - the list of command

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname = host,
                   username = user,
                   password = pswd,
                   look_for_keys =False,
                   allow_agent = False,
                   timeout = 5,
                   banner_timeout = 2)

    with client.invoke_shell() as ssh:

        for line in command:
            ssh.send(line + '\n')
            time.sleep(1)

        result = ssh.recv(65000).decode('utf-8')
    
    return result

if __name__ == '__main__':

    host_ip = "10.212.112.73"
    user = input("Enter the username: ")
    password = getpass.getpass()
    command = ["disp ip int brie"]
    
    print(send_command_ssh(host_ip, user, password, command))
