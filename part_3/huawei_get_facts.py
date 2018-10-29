    def get_facts(self):
        """Return a set of facts from the devices."""
        # default values.
        vendor = u'Huawei'
        uptime = -1
        serial_number, fqdn, os_version, hostname, model = (u'Unknown', u'Unknown', u'Unknown', u'Unknown', u'Unknown')

        # obtain output from device
        show_ver = self.device.send_command('display version')
        show_hostname = self.device.send_command('display current-configuration | inc sysname')
        show_int_status = self.device.send_command('display interface brief')

        # serial_number/IOS version/uptime/model
        for line in show_ver.splitlines():
            if 'VRP (R) software' in line:
                search_result = re.search(r"\((?P<serial_number>CE\S+)\s+(?P<os_version>V\S+)\)", line)
                if search_result is not None:
                    serial_number = search_result.group('serial_number')
                    os_version = search_result.group('os_version')

            if 'HUAWEI' in line and 'uptime is' in line:
                search_result = re.search(r"CE\S+", line)
                if search_result is not None:
                    model = search_result.group(0)
                uptime = self._parse_uptime(line)
                break

        if 'sysname ' in show_hostname:
            _, hostname = show_hostname.split("sysname ")
            hostname = hostname.strip()

        # interface_list filter
        interface_list = []
        if 'Interface' in show_int_status:
            _, interface_part = show_int_status.split("Interface")
            re_intf = r"(?P<interface>\S+)\s+(?P<physical_state>down|up|offline|\*down)\s+" \
                      r"(?P<protocal_state>down|up|\*down)"
            search_result = re.findall(re_intf, interface_part, flags=re.M)
            for interface_info in search_result:
                interface_list.append(interface_info[0])

        return {
            'uptime': int(uptime),
            'vendor': vendor,
            'os_version': py23_compat.text_type(os_version),
            'serial_number': py23_compat.text_type(serial_number),
            'model': py23_compat.text_type(model),
            'hostname': py23_compat.text_type(hostname),
            'fqdn': fqdn,  # ? fqdn(fully qualified domain name)
            'interface_list': interface_list
        }