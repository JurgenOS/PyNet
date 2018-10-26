import napalm

driver = napalm.get_network_driver('ce')
ios_ssh = driver('192.168.73.250','user','cisco')
ios_ssh.open()

for key, value in ios_ssh.get_facts().items():
    print("{}: {}".format(key, value))