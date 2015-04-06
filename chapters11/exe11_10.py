#!/usr/bin/env python
import os 
files = filter(lambda x: x and x[0] !='.',os.listdir('aaa'))
print os.listdir('aaa') #show all the files include the hide files
print files #show the files under the floder but not the hide files
