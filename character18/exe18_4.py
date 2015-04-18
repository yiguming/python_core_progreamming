import threading
import time
 
print "single threading:"
count = 0
timeBegin = time.clock()
for i in range(10):
    with open("data.txt") as fobj:
        for item in fobj:
            count += item.count("os")
timeEnd = time.clock()
print "os occures:%d" % count
print "using" , (timeEnd - timeBegin),"s"
 
print "multiple threading:"
count = 0
def read(count):
    with open("data.txt") as fobj:
        for item in fobj:
            count += item.count("os")
threads = []
timeBegin = time.clock()
for i in range(10):
    t = threading.Thread(target = read, args = (count,))
    threads.append(t)
for i in range(10):
    threads[i].start()
for i in range(10):
    threads[i].join()
timeEnd = time.clock()
print "os occures:%d" % count
print "using",(timeEnd - timeBegin),"s"      
