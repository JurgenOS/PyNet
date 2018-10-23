import telnetlib
import time


def send_command_telnet(host, user, password, command):
    # host - the ip address of the host in str format "1.1.1.1"
    # commad - the list of command
    # the function returns 'tn.read_all()' output
    # returns command output in utf-8 format

    tn = telnetlib.Telnet(host)
    tn.expect([b"Username: ", b"login: ", b"login as: "])
    tn.write(user.encode("utf-8") + b"\n")
    tn.write(password.encode("utf-8") + b"\n")

    #if password:
    #    tn.expect([b"Password: ", b"password: "])
    #    tn.write(password.encode("utf-8") + b"\n")

    time.sleep(1)
    tn.expect([b"#", b">"])
    tn.write(b"terminal length 0\n")
    tn.write(b"\n")    

    for line in command:
        tn.write(line.encode("utf-8") + b"\n")
        time.sleep(2)

    tn.write(b"\x1A") # send ^Z
    tn.write("\n".encode("utf-8"))
    time.sleep(1)
    tn.write(b"q\n")
    tn.write(b" exit\n")

    res = tn.read_all()

    tn.close()
        
    return res.decode("utf-8")


if __name__ == "__main__":
    user = "user"
    password = "cisco"
    host = "192.168.73.200" # !!ASR!! 
    command = ["show version"]
    
    print(send_command_telnet(host, command, user, password))
