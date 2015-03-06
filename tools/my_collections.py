class BQueue:
    def __init__(self, initial=None):
        self.queue = initial if initial is list else list()
        self.size = len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1

    def dequeue(self):
        self.queue.pop(0)
        self.size -= 1

