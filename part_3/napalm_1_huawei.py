import json
import napalm

driver = napalm.get_network_driver('ce')
huawei_ssh = driver('192.168.73.250','user','cisco')
huawei_ssh.open()

commands = ['disp bgp peer']

output = huawei_ssh.cli(commands)

print(output['disp bgp peer'])

huawei_ssh.close()

#for key, value in ios_ssh.get_facts().items():
#    print("{}: {}".format(key, value))