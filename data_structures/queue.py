class Queue:
    def put(self, item):
        """
        put element to the queue
        """
        raise NotImplementedError()

    def get(self):
        """
        get element from queue, but doesn't remove it
        """
        raise NotImplementedError()

    def remove(self):
        """
        remove element from queue
        """
        raise NotImplementedError()

    def __bool__(self):
        """
        returns true if there is at least one element in queue
        """
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __next__(self):
        raise NotImplementedError()


class PriorityQueue:
    def put(self, item, priority):
        """
        put element to the queue according to it's priority
        """
        raise NotImplementedError()

    def get(self):
        """
        get element from queue, but doesn't remove it
        """
        raise NotImplementedError()

    def remove(self):
        """
        remove element from queue
        """
        raise NotImplementedError()

    def __bool__(self):
        """
        returns true if there is at least one element in queue
        """
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __next__(self):
        raise NotImplementedError()
