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

    print(host)
#    print(host['port'])

    if not ping.py_ping(host['host']):
        print(host['host'], ' is unreachable!!')
        continue