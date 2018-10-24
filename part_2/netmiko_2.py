from netmiko import ConnectHandler

'''
(ip=u'', host=u'', username=u'', password=u'', secret=u'', port=None, device_type=u'', verbose=False, global_delay_factor=1, use_keys=False, key_file=None, pkey=None, passphrase=None, allow_agent=False, ssh_strict=False, system_host_keys=False, alt_host_keys=False, alt_key_file=u'', ssh_config_file=None, timeout=100, session_timeout=60, auth_timeout=None, blocking_timeout=8, keepalive=0, default_enter=None, response_return=None, serial_settings=None, fast_cli=False, session_log=None, session_log_record_writes=False, session_log_file_mode=u'write', allow_auto_change=False, encoding=u'ascii')
'''

host_telnet = {'ip': '192.168.73.201',
        'username': 'user',
        'password': 'cisco',
        'device_type': 'cisco_ios', #  ssh
        }


host_ssh = {'ip': '192.168.73.200',
        'username': 'user',
        'password': 'cisco',
        'device_type': 'cisco_ios_telnet', #  telnet
        }


hosts_list = [host_ssh, host_telnet]

for host in hosts_list:

    print('='*20)
    print('Configuring {}'.format(host['ip'])) 
    connect = ConnectHandler(**host)
    
    commands_list = []

    for i in range(11):

        commands = ['int loop {}'.format(str(i)),
                    'description test netmiko_1'
                    'ip address 1.1.1.{} 255.255.255.255'.format(str(i))
                   ]
        commands_list.append(commands) 
    
    output = connect.send_config_set(commands_list)
    print(output)

    output = connect.send_command('show ip int brief | inc loop')
    print(output)