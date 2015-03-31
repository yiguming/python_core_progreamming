#/usr/bin/env python
# -*- coding: utf8 -*-
d1 = { }
d2 = { }
while True:
    name = raw_input('name ( .is to end) :')
    if name == '.':
        break
    pid =raw_input('id:')
    d1[name] =pid
    d2[pid] = name

for key in sorted(zip(*d1.items())[0]):
                print key , d1[key]

for key in sorted(zip(*d2.items())[0]):
                print key , d2[key]

