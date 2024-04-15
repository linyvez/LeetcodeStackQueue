"""Implementation of Stack using my Queue"""

from collections import deque

class MyStack(object):
    """MyStack"""

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        queue = deque()
        while len(self.queue) != 1:
            queue.append(self.queue.popleft())
        el = self.queue.popleft()
        self.queue = queue
        return el

    def top(self):
        """
        :rtype: int
        """
        el = self.pop()
        self.push(el)
        return el

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
