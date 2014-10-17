#!/usr/bin/env python
import sys
import os
rootused=os.popen('df -h').read()
rootused1=rootused.split('\n')
#print rootused      
#print type(rootused)  #str havesplitlistno have split
#print rootused1
#print type(rootused1)
for rootused2 in rootused1:
  #print rootused2  #rootused2 change str have split
  rootused2=rootused2.split()
  if len(rootused2) <= 1:     #chu li zi fu chuang chang du bu yi yang qing kuang
                continue
  #print '------%s' %rootused2
#  print rootused2[4]
#  print rootused2[4][0:2]
  rootused3=rootused2[4][0:2]
  if rootused3.isdigit() == False:
    continue
  else:
    rootused3=int(rootused3)
    if rootused3 > 80:
#      print rootused3
      os.system("/usr/bin/python  /tmp/clealogs.py")
