# Way 1:
stack = []
stack.append(1)
stack.append(5)
stack.append(10)
stack.append(28)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

import time

from memory_profiler import profile


class stack(list):
    @profile
    def push(self, data):
        self.append(data)

    @profile
    def is_empty(self):
        return len(self) == 0

    @profile
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("No current stack exists")

    @profile
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("No current stack exists")


t1 = time.time()
s1 = stack()
s1.push(5)
s1.push(10)
s1.push(12)
s1.push(1)
print(s1.peek())
t2 = time.time()
print("Total time for exec:", t2 - t1)


from collections import deque

t3 = time.time()
st = deque()
st.append(4)
st.append(5)
st.appendleft(10)
print(st.__len__())
print(st)
st.pop()
st.popleft()
print(st)
st.append(15)
st.append(12)
st.append([1, 2, 3, 4])
print(st)
t4 = time.time()

print("Time using deque:", t4 - t3)
