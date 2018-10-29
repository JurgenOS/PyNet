from multiping import MultiPing

def py_ping(ip_address):

    '''
    In this case ip_address is a string to be converted onto a list with only one argumeny(ip address)
    to return just True or False
    TODO:
    rewrite script to take the list with many ip addresses
    '''
    ip_adresses_list = []
    ip_adresses_list.append(ip_address)
    mp = MultiPing(ip_adresses_list)
    mp.send()
    responses, no_responses = mp.receive(1)
    if responses:
        return True
    if no_responses:
         return False

           
if __name__ == '__main__':
    test = py_ping(["8.8.8.8", "youtube.com", "127.0.0.1", "192.168.100.100"])
    print(test)
    test = py_ping(["192.168.100.100"])
    print(test)
    