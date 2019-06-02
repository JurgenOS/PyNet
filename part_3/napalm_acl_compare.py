import napalm


driver = napalm.get_network_driver('ios')

node = driver('192.168.73.201','user','cisco')
node.open()
        
node.load_merge_candidate(config='hostname test\ninterface Ethernet2\ndescription bla')
#node.load_merge_candidate(filename = 'acl_config.txt')
diffs = node.compare_config() 
print(diffs)

node.close()