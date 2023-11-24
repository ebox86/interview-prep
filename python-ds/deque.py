from collections import deque
d = deque('ghi')  # make a new deque with three items
for elem in d:   # iterate over the deque's elements
    print(elem.upper())
