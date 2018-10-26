# PyNet
The repo to keep code from course "Python for network engineers" by David Bonamal

before start coding type this to get recent environment
```
 apt update && apt upgrade
 apt-get update && apt-get upgrade
 apt install sudo
 sudo apt-get install -y software-properties-common
 add-apt-repository ppa:jonathonf/python-3.6
 sudo apt-get update
 sudo apt-get install python3.6
```
to install pip:
```
# apt-get install wget
# wget https://bootstrap.pypa.io/get-pip.py
# sudo python3.6 get-pip.py
```
or if you do it second and more time, just type:
```
# sudo python3.6 /root/Download/get-pip.py
```

### Git Inatallatoin
```
# sudo apt-get install git
# git config --global user.name "Your Name"
# git config --global user.email "youremail@domain.com"
# git remote origin https://github.com/JurgenOS/PyNet.git   (for first time)
# git fetch
# git pull
```
to see the list of remote git repos:
```
# git remote -v
```
### Docker

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
### Whishlist
- [ ] install paramiko into pyneng for python2
- [ ] install napalm, napalm-ce
- [ ] install this:
```
apt-get update
apt-get install python -y
apt-get install build-essential libssl-dev libffi-dev -y
apt-get install python-pip -y
pip install cryptography
pip install netmiko
pip install pyntc

pip install ipython
pip install tabulate
pip install simplejson
pip install ipython
apt-get install graphviz
pip install graphviz
pip install pyyaml
pip install pexpect
pip install paramiko
pip install jinja2
pip install textfsm
pip install ansible
pip install ntc-ansible
==========================================
python -m pip install -U pip
python -m pip install -U matplotlib
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
pip install openpyxl
pip install xlrd
pip install xlwt
pip install XlsxWrite
```
to check installed packets:
```
lssitepackages
```
