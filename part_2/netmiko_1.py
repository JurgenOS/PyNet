from netmiko import ConnectHandler

'''
(ip=u'', host=u'', username=u'', password=u'', secret=u'', port=None, device_type=u'', verbose=False, global_delay_factor=1, use_keys=False, key_file=None, pkey=None, passphrase=None, allow_agent=False, ssh_strict=False, system_host_keys=False, alt_host_keys=False, alt_key_file=u'', ssh_config_file=None, timeout=100, session_timeout=60, auth_timeout=None, blocking_timeout=8, keepalive=0, default_enter=None, response_return=None, serial_settings=None, fast_cli=False, session_log=None, session_log_record_writes=False, session_log_file_mode=u'write', allow_auto_change=False, encoding=u'ascii')
'''

host = {'ip': '192.168.73.201',
        'username': 'user',
        'password': 'cisco',
        'device_type': 'cisco_ios', #  ssh
        }

connect = ConnectHandler(**host)
output = connect.send_command('show ip int brief')
print(output)

commands = ['int loop 1',
            'description test netmiko_1'
            'ip address 1.1.1.1 255.255.255.255'
           ]

output = connect.send_config_set(commands)
print(output)

