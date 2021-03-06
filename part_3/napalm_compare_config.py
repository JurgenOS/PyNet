import json
import napalm
import ping

hosts = [{'host' : '192.168.206.201',
          'vendor':'cisco',
          'port':'telnet'
         },
         {'host': '192.168.206.202',
          'vendor':'cisco',
          'port':'ssh'
         },
         {'host': '192.168.206.203',
          'vendor':'cisco',
          'port':'telnet'
         }        
        ]

for host in hosts:

    if not ping.py_ping(host['host']):
        print(host['host'], ' is unreachable!!')
        continue

    print('='*60)
    print('''host      : {}
vendor    : {}
admin_port: {}
'''.format(host['host'], host['vendor'], host['port']))

    if host['vendor'] == 'cisco':
        driver = napalm.get_network_driver('ios')
        optional_args = {'transport': '{}'.format(host['port']),}
        node = driver('{}'.format(host['host']),'user','cisco', optional_args = optional_args)
        node.open()
        
        node.load_merge_candidate(filename='ACL1.cfg')
        
        diffs = node.compare_config()
        if len(diffs) > 0:
            print(diffs)
            node.commit_config()
        else:
            print('No changes required.')
            node.discard_config()
        
        node.close()
        
        
        
    if host['vendor'] == 'huawei':
        driver = napalm.get_network_driver('ce')
        optional_args = {'transport': '{}'.format(host['port']),}
        node = driver('{}'.format(host['host']),'user','cisco', optional_args = optional_args)
        node.open()
        print (json.dumps(node.cli('disp bgp peer'), indent = 4), '\n')
        node.close()