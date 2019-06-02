import json
import napalm


driver = napalm.get_network_driver('ios')
ios_ssh = driver('192.168.73.201','user','cisco')


ios_ssh.open()

#for key, value in ios_ssh.get_facts().items():
#    print("{}: {}".format(key, value))

output = ios_ssh.get_route_to(destination = '192.168.73.200')
print (json.dumps(output, indent = 4))



'''
>>> from napalm import get_network_driver
>>> driver = get_network_driver('eos')
>>> optional_args = {'my_optional_arg1': 'my_value1', 'my_optional_arg2': 'my_value2'}
>>> device = driver('192.168.76.10', 'dbarroso', 'this_is_not_a_secure_password', optional_args=optional_args)
>>> device.open()

===============================
allow_agent (ios, iosxr, nxos_ssh) - Paramiko argument, enable connecting to the SSH agent (default: False).
alt_host_keys (ios, iosxr, nxos_ssh) - If True, host keys will be loaded from the file specified in alt_key_file.
alt_key_file (ios, iosxr, nxos_ssh) - SSH host key file to use (if alt_host_keys is True).
auto_rollback_on_error (ios) - Disable automatic rollback (certain versions of IOS support configure replace, but not rollback on error) (default: True).
config_lock (iosxr, junos) - Lock the config during open() (default: False).
canonical_int (ios) - Convert operational interface’s returned name to canonical name (fully expanded name) (default: False).
dest_file_system (ios) - Destination file system for SCP transfers (default: flash:).
enable_password (eos) - Password required to enter privileged exec (enable) (default: '').
global_delay_factor (ios, nxos_ssh) - Allow for additional delay in command execution (default: 1).
ignore_warning (junos) - Allows to set ignore_warning when loading configuration to avoid exceptions via junos-pyez. (default: False).
keepalive (iosxr, junos) - SSH keepalive interval, in seconds (default: 30 seconds).
key_file (ios, iosxr, junos, nxos_ssh) - Path to a private key file. (default: False).
port (eos, ios, iosxr, junos, nxos, nxos_ssh) - Allows you to specify a port other than the default.
secret (ios, nxos_ssh) - Password required to enter privileged exec (enable) (default: '').
ssh_config_file (ios, iosxr, junos, nxos_ssh) - File name of OpenSSH configuration file.
ssh_strict (ios, iosxr, nxos_ssh) - Automatically reject unknown SSH host keys (default: False, which means unknown SSH host keys will be accepted).
transport (eos, ios, nxos) - Protocol to connect with (see The transport argument for more information).
use_keys (ios, iosxr, nxos_ssh) - Paramiko argument, enable searching for discoverable private key files in ~/.ssh/ (default: False).
eos_autoComplete (eos) - Allows to set autoComplete when running commands. (default: None equivalent to False)
'''