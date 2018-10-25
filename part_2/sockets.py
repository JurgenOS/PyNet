import time
import socket
import re

def pars_vendor(string):

    reg = re.compile(b'-(?P<Vendor>[A-Za-z]+)[-_]')
    if reg.search(string):
        return reg.search(string).group('Vendor')

    elif string == b'SSH-2.0--\r\n':return b'HUAWEI'
    else:
        #print("VENDOR isn't DETECTED")
        return b"NOT DETECTED"

def socket_checker(host_ip):

    # host_ip = '192.168.73.200'
    # script return dictionary in format:     
    # res = {'ip addr':'{}','SSH':'','Telnet':'', 'Vendor':''}

    res = {'ip addr':'{}'.format(host_ip),
           'SSH':None,
           'Telnet':None,
           'Vendor':None
          }  

    ports = {'Telnet': 23,
             'SSH':22
            }

    reach = None

    for protocol, port in ports.items():

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(3)
        

        
        try:
            clientSocket.connect((host_ip, port))

        except socket.timeout as timeout:
            continue
        except ConnectionRefusedError as reject:
            continue
        except TimeoutError as not_response:
            print(' HOST {} is not reachable by PORT {}'.format(host_ip, port))

        output = clientSocket.recv(1024)
            
        if output:
            res['protocol'] = str(protocol)

            if port == 22:
                res['Vendor'] = pars_vendor(output).decode('utf-8')
                res['SSH'] = 'SSH'
                reach = 'SSH'
            elif port == 23:
                res['Telnet'] = 'Telnet'
                reach = 'Telnet'
        clientSocket.close()

        if reach:
            return res
        else:
            return "host isn't reachable"

if __name__ == '__main__':

    #GNS3 Cisco telnet
    print(socket_checker('192.168.73.200'))
    print()

    #GNS3 Cisco ssh
    print(socket_checker('192.168.73.201'))
    print()

    #eNSP HUAWEI
    print(socket_checker('192.168.73.250'))
    print()

    #poligon ssh  10.183.2.180
    #print(socket_checker('10.183.2.180'))
    #print()

    #huawei ssh 10.212.112.73
    #print(socket_checker('10.212.112.73'))
    #print()

    #huawei ssh 10.155.254.214 !WRONG!
    #print(socket_checker('10.155.254.214'))
    #print()
    
    #huawei telent 10.155.254.214 !WRONG!. It returns this:
    #b'\xff\xfb\x01\xff\xfb\x01\xff\xfb\x01\xff\xfb\x03\xff\xfd\x18\xff\xfd\x1f'
    #print(socket_checker('10.155.254.214'))
    #print()

    #Cisco Telnet 10.155.254.214
    #print(socket_checker('10.155.154.177'))
    #print()

    #lines = [b'SSH-2.0-ZTE_SSH.2.0\n', b'SSH-1.99-Cisco-1.25\n', b'SSH-2.0-HUAWEI-1.5\n', b'SSH-2.0--\r\n']
    #for line in lines: 
    #    print(pars_vendor(line))
    
    '''
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
    #poligon ssh  10.183.2.180
    print(socket_checker('10.183.2.180'))
    print()

    line = b'SSH-1.99-Cisco-1.25\n'
    print(pars_vendor(line))

    ============
    b'SSH-2.0-HUAWEI-1.5\n'
    b'SSH-2.0-VRP-3.3\n' #h3c
    b'SSH-1.99-Cisco-1.25\n'
    b'SSH-2.0-ROSSSH\r\n'# Mikrot
    b'SSH-2.0-ZTE_SSH.2.0\n' #Poligon
    b'SSH-2.0--\r\n' # HUAWEI?
    b'SSH-1.99-DOPRA-1.5\n' # HUAWEI?
    '''
