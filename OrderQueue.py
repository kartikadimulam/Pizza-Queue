from PizzaOrder import PizzaOrder

class OrderQueue:

    def __init__(self):
        self.orderqueue = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            # item can't be greater than parent
            if self.orderqueue[i].time < self.orderqueue[i // 2].time:
                # initiate switch
                tmp = self.orderqueue[i // 2]
                self.orderqueue[i // 2] = self.orderqueue[i]
                self.orderqueue[i] = tmp
                i = i // 2
                # switches to the parent now, going up the tree

    def addOrder(self, pizzaOrder):
        self.orderqueue.append(pizzaOrder)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
            
    def percDown(self, i):
        # checking if children exist
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            # can't be greater than the child
            if self.orderqueue[i].time > self.orderqueue[mc].time:
                # initiate switch
                tmp = self.orderqueue[i]
                self.orderqueue[i] = self.orderqueue[mc]
                self.orderqueue[mc] = tmp
            i = mc
            # switches to the kid now, going down the tree

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.orderqueue[i*2].time < self.orderqueue[i*2+1].time:
                return i * 2
            else:
                return i * 2 + 1

    def processNextOrder(self):
        # deleting top element
        retval = self.orderqueue[1].getOrderDescription()
        self.orderqueue[1] = self.orderqueue[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.orderqueue.pop()
        self.percDown(1)
        return retval

class QueueEmptyException(Exception):
    pass
