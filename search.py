#!/usr/env python
import os
def Search(path):
	for root,dirs,files in os.walk(path):
		for filespath in files:
			if 'test' in filespath:
				print os.path.join(root,filespath)
if __name__=="__main__":
	path="/root/python"
Search(path)
