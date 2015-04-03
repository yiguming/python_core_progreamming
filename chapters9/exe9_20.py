#!/usr/bin/env python
import zipfile
with zipfile.ZipFile("hello.zip","w") as myzip:
    myzip.write("hello.txt")



