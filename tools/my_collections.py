class BQueue:
    """A basic queue implementation."""
    def __init__(self, initial=None):
        self.queue = initial if initial is list else list()
        self.size = len(self.queue)

    def enqueue(self, value):
        """Adds an element to the queue."""
        self.queue.append(value)
        self.size += 1

    def dequeue(self):
        """Gets the first element from the queue and remove it afterwords."""
        self.queue.pop(0)
        self.size -= 1

