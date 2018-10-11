# PyNet
The repo to keep code from course "Python for network engineers" by David Bonamal

before start coding type this to get recent environment
```
# apt get update $$ apt upgrate
# apt-get update $$ apt-get upgrate
# sudo apt-get install -y software-properties-common
# add-apt-repository ppa:jonathonf/python-3.6
# apt install sudo
# sudo apt-get update
# sudo apt-get install python3.6
```
to install pip:
```
# apt-get install wget
# wget https://bootstrap.pypa.io/get-pip.py
# sudo python3.6 get-pip.py
```


to remember how to save changes in docker container
```
#docker ps

#docker images

#docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
```
CONTAINER = docker ps

REPOSITORY[:TAG] = docker images

example:
```
#docker commit c3f279d17e0a  svendowideit/testimage:version3
```
