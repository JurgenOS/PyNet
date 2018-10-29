import json
import napalm
import ping

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
         },   
         {'host': '192.168.206.200',
          'vendor':'cisco',
          'port':'ssh'
         },        
         {'host': '192.168.206.201',
          'vendor':'cisco',
          'port':'ssh'
         },        
         {'host': '192.168.206.202',
          'vendor':'cisco',
          'port':'ssh'
         },        
         {'host': '192.168.206.203',
          'vendor':'cisco',
          'port':'ssh'
         },        
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

    if not ping.py_ping(host['host']):
        print(host['host'], ' is unreachable!!')
        continue

    print('='*60)
    print('''host      : {}
vendor    : {}
admin_port: {}
'''.format(host['host'], host['vendor'], host['port']))
    '''
    if host['vendor'] == 'cisco':
        driver = napalm.get_network_driver('ios')
        optional_args = {'transport': '{}'.format(host['port']),}
        node = driver('{}'.format(host['host']),'user','cisco', optional_args = optional_args)
        node.open()
        print (json.dumps(node.get_arp_table(), indent = 4), '\n')
        node.close()
    if host['vendor'] == 'huawei':
        driver = napalm.get_network_driver('ce')
        optional_args = {'transport': '{}'.format(host['port']),}
        node = driver('{}'.format(host['host']),'user','cisco', optional_args = optional_args)
        node.open()
        print (json.dumps(node.get_arp_table(), indent = 4), '\n')
        node.close()

    '''
   
    try:    
        if host['vendor'] == 'cisco':
            driver = napalm.get_network_driver('ios')
            optional_args = {'transport': '{}'.format(host['port']),}
            node = driver('{}'.format(host['host']),'user','cisco', optional_args = optional_args)
            node.open()
            print (json.dumps(node.get_arp_table(), indent = 4), '\n')
            node.close()

        if host['vendor'] == 'huawei':
            driver = napalm.get_network_driver('ce')
            optional_args = {'transport': '{}'.format(host['port']),}
            node = driver('{}'.format(host['host']),'user','cisco', optional_args = optional_args)
            node.open()
            print (json.dumps(node.get_arp_table(), indent = 4), '\n')
            node.close()

    except saved_exception as error:
        print(error)
        continue            
            
            
            
    except NetMikoAuthenticationException(msg) as error:
        print(error)
        continue
