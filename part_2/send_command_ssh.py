import paramiko
import getpass
import sys
import time

def send_command_ssh(host, user, pswd, command):
    # host - the ip address of the host in str format, e.g.'1.1.1.1'
    # command - the list of command
    # returns command output in utf-8 format

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

        ssh.send("terminal length 0\n")
        for line in command:
            ssh.send(line + '\n')
            time.sleep(1)

        result = ssh.recv(65000).decode('utf-8')
    
    return result


if __name__ == '__main__':

    host_ip = "192.168.88.97"
    user = 'huawei'
    password = 'huawei'
    command = ['sys',
               'sysn HUAWEI-1324567890_huawei_test_long_hostname',
               'acl 2001',
               'rule 10 permit source 10.1.0.0 0.255.255.255'
               ]
    
    print(send_command_ssh(host_ip, user, password, command))
