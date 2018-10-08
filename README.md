# PyNet
The repo to keep code from course "Python for network engineers" by David Bonamal

to remember how to save changes in docker container
'''
#docker ps

#docker images

#docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
'''
CONTAINER = docker ps
REPOSITORY[:TAG] = docker images

example:
'''
#docker commit c3f279d17e0a  svendowideit/testimage:version3
'''
