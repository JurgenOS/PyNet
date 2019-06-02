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

for host in hosts:

    if not ping.py_ping(host['host']):
        print(host['host'], ' is unreachable!!')
        continue

    print('='*60)
    print('''host      : {}
vendor    : {}
admin_port: {}
'''.format(host['host'].strip(), host['vendor'], host['port']))

    if host['vendor'] == 'cisco':
        driver = napalm.get_network_driver('ios')
        optional_args = {'transport': '{}'.format(host['port']),}
        node = driver('{}'.format(host['host'].strip()),'user','cisco', optional_args = optional_args)
        node.open()
        print (json.dumps(node.get_bgp_neighbors(), indent = 4), '\n')
        node.close()
    if host['vendor'] == 'huawei':
        driver = napalm.get_network_driver('ce')
        optional_args = {'transport': '{}'.format(host['port']),}
        node = driver('{}'.format(host['host'].strip()),'user','cisco', optional_args = optional_args)
        node.open()
        print (json.dumps(node.cli('disp bgp peer'), indent = 4), '\n')
        node.close()


'''
============================================================
host      : 192.168.73.201
vendor    : cisco
admin_port: ssh

{
    "global": {
        "router_id": "192.168.73.201",
        "peers": {
            "192.168.73.200": {
                "local_as": 65000,
                "remote_as": 65000,
                "remote_id": "192.168.73.200",
                "is_up": true,
                "is_enabled": true,
                "description": "",
                "uptime": 46,
                "address_family": {
                    "ipv4": {
                        "received_prefixes": 0,
                        "accepted_prefixes": 0,
                        "sent_prefixes": 0
                    }
                }
            },
            "192.168.73.250": {
                "local_as": 65000,
                "remote_as": 65000,
                "remote_id": "192.168.73.250",
                "is_up": true,
                "is_enabled": true,
                "description": "",
                "uptime": 113,
                "address_family": {
                    "ipv4": {
                        "received_prefixes": 0,
                        "accepted_prefixes": 0,
                        "sent_prefixes": 0
                    }
                }
            }
        }
    }
}

============================================================
'''