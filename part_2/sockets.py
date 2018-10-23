def socket_checker(host_ip):
    # host_ip = '192.168.73.200'
    import socket

    
    ports = {'Telnet': 23,
             'SSH':22
            }


    for protocol, port in ports.items():

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((host_ip, port))
        if clientSocket.recv(1024):
            print('{} is opened'.format(protocol))
        clientSocket.close()


if __name__ == '__main__'