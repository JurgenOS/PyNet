import socket
import re

def pars_vendor(string):

    reg = re.compile(b'-(?P<Vendor>[A-Za-z]+)-')
    return reg.search(string).group('Vendor')

def socket_checker(host_ip):




    # host_ip = '192.168.73.200'
    # script return dictionary in format:     
    # res = {'ip addr':'{}','protocol':'','output':''}

    res = {'ip addr':'{}'.format(host_ip),
           'protocol':None,
           'vendor':None
          }  

    ports = {'Telnet': 23,
             'SSH':22
            }


    for protocol, port in ports.items():

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(3)

        try:
            clientSocket.connect((host_ip, port))

        except socket.timeout as reject:
            continue
        except ConnectionRefusedError as error:
            continue
    
        output = clientSocket.recv(1024)

        if output:
            res['protocol'] = str(protocol)

            if port == 22:
                res['vendor'] = pars_vendor(output).decode('utf-8')

        clientSocket.close()
    
    return res

if __name__ == '__main__':

    #huawei ssh 10.212.112.73
    print(socket_checker('10.212.112.73'))
    print()
    #h3c ssh 10.136.45.28
    print(socket_checker('10.136.45.28'))
    print()
    #cisco telnet 10.202.59.65
    print(socket_checker('10.202.59.65'))
    print()
    #cisco ssh 10.202.59.65
    print(socket_checker('10.202.59.65'))
    print()    
    #poligon telnet 10.171.101.250
    print(socket_checker('10.171.101.250'))
    print()
    '''
    line = b'SSH-1.99-Cisco-1.25\n'
    print(pars_vendor(line))
    '''
