class ArrayList:
    """
    use 'array' module to create array data structure
    this list works only with items with the same type
    """

    def add_front(self, item):
        """
        add item to front of the list (create new head)
        """

    def insert(self, item, index):
        """
        add new item to the middle of linked list
        raise exception if index is out of list size
        """
        raise NotImplementedError()

    def add_back(self, item):
        """
        add item to back of the list (create new tail)
        """

    def head(self):
        """
        return head of linked list
        """
        raise NotImplementedError()

    def tail(self):
        """
        return tail of linked list
        """
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __next__(self):
        raise NotImplementedError()


class LinkedList:
    def add_front(self, item):
        """
        add item to front of the list (create new head)
        """
        raise NotImplementedError()

    def add_back(self, item):
        """
        add item to back of the list (create new tail)
        """

    def insert(self, item, index):
        """
        add new item to the middle of linked list
        raise exception if index is out of list size
        """
        raise NotImplementedError()

    def head(self):
        """
        return head of linked list
        """
        raise NotImplementedError()

    def tail(self):
        """
        return tail of linked list
        """
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __next__(self):
        raise NotImplementedError()


class Deque:
    def add_front(self, item):
        """
        add item to front of the deque (create new head)
        """
        raise NotImplementedError()

    def insert(self, item, index):
        """
        add new item to the middle of deque
        raise exception if index is out of deque size
        """
        raise NotImplementedError()

    def add_back(self, item):
        """
        add item to back of the deque (create new tail)
        """
        raise NotImplementedError()

    def head(self):
        """
        return head of the deque
        """
        raise NotImplementedError()

    def tail(self):
        """
        return tail of the deque
        """
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        """iterator from head to tail"""
        raise NotImplementedError()

    def __next__(self):
        raise NotImplementedError()
