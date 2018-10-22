import telnetlib
import time


def send_command_telnet(hosts, command, user, password):
    # hosts - the list of hosts
    # commad - the list of command
    # the function returns 'tn.read_all()' output

    for node in hosts:
        tn = telnetlib.Telnet(node)
    
        #tn.read_until(b"Username: ")
        tn.expect([b"Username: ", b"login: "])
        tn.write(user.encode("utf-8") + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode("utf-8") + b"\n")
    
        for item in  command:
            tn.write(item.encode("utf-8") + b"\n")
            time.sleep(2)
     
        res = tn.read_all()
        tn.close()

        return res


if __name__ == "__main__":
    user = "user"
    password = "cisco"
    hosts = ["192.168.73.200"]
    command = [" show version", " exit"]
    
    print(send_command_telnet(hosts, command, user, password))