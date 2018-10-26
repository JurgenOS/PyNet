import json
import napalm

driver = napalm.get_network_driver('ios')
optional_args = {'transport': 'telnet',}
ios_telnet = driver('192.168.73.200','user','cisco', optional_args = optional_args)


ios_telnet.open()

for key, value in ios_telnet.get_facts().items():
    print("{}: {}".format(key, value))

'''
#output = ios_telnet.get_interfaces()
#print (json.dumps(output, indent = 4))


'''