import subprocess

def check_ping(host):
    response = subprocess.run("ping -c 2 {}".format(host), 
                              shell = True,
                              stdout = subprocess.DEVNULL)

    if response.returncode == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    if check_ping("google.com"):
        print("Internet is reachble \n")
    if check_ping ("192.168.206.1"):
        print("the getway is rachable \n")
