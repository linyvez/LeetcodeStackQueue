"""Implementation of the Queue using my own Stacks"""

from collections import deque

class MyQueue(object):
    """MyQueue"""

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)


    def pop(self):
        """
        :rtype: int
        """
        stack = deque()
        while not self.empty():
            stack.append(self.stack.pop())
        output = stack.pop()
        while len(stack) != 0:
            self.push(stack.pop())
        return output


    def peek(self):
        """
        :rtype: int
        """
        stack = deque()
        while not self.empty():
            stack.append(self.stack.pop())
        el = stack.pop()
        stack.append(el)
        while len(stack) != 0:
            self.push(stack.pop())
        return el


    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.stack) == 0 else False
