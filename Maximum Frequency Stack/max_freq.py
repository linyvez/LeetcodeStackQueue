"""Implementation of Maximum Frequency Stack"""
from collections import deque, defaultdict

class FreqStack(object):
    """FreqStack class"""

    def __init__(self):
        self.freqstack = deque()
        self.frequencies = defaultdict(int)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freqstack.append(val)
        self.frequencies[val] += 1

    def pop(self):
        """
        :rtype: int
        """
        temp = deque()
        maximum_frequency = max(self.frequencies.values())
        output = None

        while self.freqstack:
            el = self.freqstack.pop()
            temp.append(el)
            if self.frequencies[el] == maximum_frequency:
                output = el
                break
        self.frequencies[output] -= 1
        while temp:
            el_ = temp.pop()
            if el_ != output:
                self.freqstack.append(el_)
        return output
    #     temp = deque()
    #     good = deque()
    #     maximum_frequency = max(self.frequencies.values())
    #     while self.freqstack:
    #         el = self.freqstack.pop()
    #         if self.frequencies[el] == maximum_frequency:
    #             good.append(el)
    #         temp.append(el)
    #     temp2 = deque()
    #     for el in temp:
    #         temp2.append(el)
    #     stop = False
    #     while temp2 and not stop:
    #         current = temp2.popleft()
    #         for g in good:
    #             if g == current:
    #                 needed = current
    #                 stop = True
    #     output = needed
    #     self.frequencies[output] -= 1
    #     while temp:
    #         el_ = temp.popleft()
    #         if el_ == needed:
    #             needed = None
    #             continue
    #         self.freqstack.append(el_)
    #     while self.freqstack:
    #         temp.append(self.freqstack.pop())
    #     self.freqstack = temp
    #     return output

# obj = FreqStack()
# obj.push(5)
# obj.push(7)
# obj.push(5)
# obj.push(7)
# obj.push(4)
# obj.push(5)


# param_2 = obj.pop()
# print(obj, param_2) # [5,7,5,7,4] 5
# param_3 = obj.pop()
# print(obj, param_3) # [5,7,5,4] 7
# param_4 = obj.pop()
# print(obj, param_4) # [5,7,4] 5
# param_5 = obj.pop()
# print(obj, param_5) # [5,7] 4
