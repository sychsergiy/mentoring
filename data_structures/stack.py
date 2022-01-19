class Stack:
    def pop(self):
        """
        return item from stack and removes it,
        None if stack is empty
        """
        raise NotImplementedError()

    def push(self, item):
        """
        add item to stack
        """
        raise NotImplementedError()

    def peek(self):
        """
        return item from stack (doesn't remove it),
        None if stack is empty
        """
        raise NotImplementedError()

    def __len__(self):
        """
        return amount of items in stack
        """
        raise NotImplementedError()

    def __bool__(self):
        """
        return true if stack is empty
        """
        raise NotImplementedError()
