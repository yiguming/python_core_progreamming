#!/usrbin/env python
class Queue(object):
    def __init__(self,queue):
        self.queue = queue
    def enqueue(self,element):
        self.queue.append(element)
    def dequeue(self):
        firstelement = self.queue[0]
        self.queue = self.queue[1:]
        return firstelement
    def __str__(self):
        return str(self.queue)
    __repr__ = __str__

if __name__ == "__main__":
    que = Queue([1,2,3,4])
    print que
    que.enqueue(5)
    print que
    print que.dequeue()
    print que
