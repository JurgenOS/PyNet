import json
import napalm


hosts = [{'host' : '192.168.73.200',
          'vendor':'cisco',
          'port':'telnet'
         },
         {'host': '192.168.73.201',
          'vendor':'cisco',
          'port':'ssh'
         },
         {'host': '192.168.73.250',
          'vendor':'huawei',
          'port':'ssh'
         }   
        ]

'''
hosts = [{'host' : '192.168.73.200',
          'vendor':'cisco',
          'port':'telnet'
         }   
        ]
'''
for host in hosts:

#    print(host)
#    print(host['port'])



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
        print (json.dumps(node.ping('192.168.73.1'), indent = 4), '\n')
    
    if host['vendor'] == 'huawei':
        driver = napalm.get_network_driver('ce')
        optional_args = {'transport': '{}'.format(host['port']),}
        node = driver('{}'.format(host['host']),'user','cisco', optional_args = optional_args)

        node.open()
        print (json.dumps(node.ping('192.168.73.1'), indent = 4), '\n')
