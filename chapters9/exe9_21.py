#!/usr/bin/python
import os
import zipfile

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

if __name__ == '__main__':
    zip = zipfile.ZipFile('Python.zip', 'w')
    zipdir('/home/qiezi/python/python_core_progreamming/chapters9', zip)
    zip.close()
