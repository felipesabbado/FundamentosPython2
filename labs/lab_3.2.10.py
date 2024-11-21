# Queue aka FIFO: part 2
""" Your task is to slightly extend the Queue class's capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.
Expected output:
    1
    dog
    False
    Queue empty
"""

# Choose base class for the new exception.
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, elem):
        self.__queue_list.insert(0, elem)


    def get_queue(self):
        return self.__queue_list

    def get(self):
        if len(self.__queue_list) > 0:
            elem = self.__queue_list[-1]
            del self.__queue_list[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def is_empty(self):
        return len(self.get_queue()) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.is_empty():
        print(que.get())
    else:
        print("Queue empty")
