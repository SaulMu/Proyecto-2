

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return f'{list(self.queue)}'
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
 
    # for popping an element based on Priority
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[max_val][0]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item[0], item[1], item[2] 
        except IndexError:
            print()
            exit()

    def update(self, data):
        item = data[1]
        for i in range(len(self.queue)): 
            if self.queue[i][1] == item:
                self.queue[i] = data
                break

    def value(self, node):
        for i in range(len(self.queue)): 
            if self.queue[i][1] == node:
                return self.queue[i][0]
            
'''
q = PriorityQueue()
for i in range(5):
    q.insert((float('inf'),i,(0,0)))

q.update((0,0,(0,0)))

er = q.value(0)
print(er)
'''