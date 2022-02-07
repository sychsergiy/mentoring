import array

class ArrayList:
    """
    use 'array' module to create array data structure
    this list works only with items with the same type
    """

    def __init__(self):
        self.items = array.array('i')

    def add_front(self, item):
        """
        add item to front of the list (create new head)
        """
        extended_items = [None] * (len(self) + 1)
        extended_items[0] = item
        extended_items[1:] = self.items[:]

        self.items = extended_items

    def insert(self, item, index):
        """
        add new item to the middle of array list
        raise exception if index is out of list size
        """
        if index > len(self):
            raise IndexError

        if index == 0:
            self.add_front(item)
            return

        if index == len(self):
            self.add_back(item)
            return

        extended_items = [None] * (len(self) + 1)
        extended_items[:index] = self.items[:index]
        extended_items[index] = item
        extended_items[index+1:] = self.items[index:]

        self.items = extended_items
        

    def add_back(self, item):
        """
        add item to back of the list (create new tail)
        """
        extended_items = [None] * (len(self)+1)
        extended_items[:len(self)] = self.items[:]
        extended_items[len(self)] = item

        self.items = extended_items

    def head(self):
        """
        return head of array list
        """
        return self.items[0]

    def tail(self):
        """
        return tail of array list
        """
        return self.items[len(self)-1]

    def __len__(self):
        size = 0
        for i in self.items:
            size+=1
        return size

    # def __iter__(self):
    #     for i in self.items:
    #         yield i

    # def __next__(self):
    #     for i in self.items:
    #         yield i


class LinkedList:
    class __Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

    def __init__(self):
        self.head = None

    def add_front(self, item):
        new_node = self.__Node(item, self.head)
        self.head = new_node

    def add_back(self, item):
        new_node = self.__Node(item)
        if self.head is None:
            self.head = new_node
            return

        last = self.tail()
        last.next = new_node

    def insert(self, item, index):
        """
        add new item to the middle of linked list
        raise exception if index is out of list size
        """
        if index > len(self):
            raise Exception

        if index == 0:
            self.add_front(item)

        if index == len(self):
            self.add_back(item)

        new_node = self.__Node(item)
        current = self.head
        while (self.head) and index > 0:
            current = current.next
            index -= 1

        new_node.next = current.next
        current.next = new_node


    def head(self):
        return self.head

    def tail(self):
        last = self.head
        while (last.next):
            last = last.next
        return last

    def __len__(self):
        size = 0
        last = self.head
        while (last.next):
            size += 1
            last = last.next
        return size
        

    # def __iter__(self):
    #     current = self.head
    #     while current:
    #         yield current
    #         current = current.next

    # def __next__(self):
    #     current = self.head
    #     while current:
    #         current = current.next




class Deque:

    def __init__(self):
        self.items = array.array('i')

    def add_front(self, item):
        """
        add item to front of the deque (create new head)
        """
        self.items.append(item)

    def insert(self, item, index):
        """
        add new item to the middle of deque
        raise exception if index is out of deque size
        """
        try:
            self.insert(index, item)
        except Exception as e:
            raise e

    def add_back(self, item):
        """
        add item to back of the deque (create new tail)
        """
        self.items.insert(0, item)

    def head(self):
        """
        return head of the deque
        """
        return self.items[len(self.items)-1]

    def tail(self):
        """
        return tail of the deque
        """
        return self.items[0]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        """iterator from head to tail"""
        return reversed(self.items)


    def __next__(self):
        raise next(reversed(self.items))
