import sys
import os
import url
logdir = '/tmp'     #test dir
#logdir = '/home/data/tomcat-7.0.42/logs'
nowdir = os.chdir(logdir)
#print os.getcwd()   #test if success chang dir
logsize = os.popen('du -s * ').read()
logsize1 = logsize.split('\n')
#print type(logsize1)   #look type
#print type(logsize)    #look type      
for size in logsize1:
        size = size.split('\t')
        if len(size) <= 1:     #chu li zi fu chuang chang du bu yi yang qing kua
ng
                continue
#       print size[0]    #look if size[0] is our dream data 
        if (200000 < int(size[0]) && int(size[0])< 1000000):
#               print size[1]  # test if success
                os.remove(size[1])
os.system('echo  > catalina.out')
