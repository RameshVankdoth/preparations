# # Method 1
# queue = []
# queue.append(1)
# queue.append(10)
# print(queue)
# queue.pop(0)
# print(queue)
# queue.append(15)
# print(queue)
# queue.pop(0)
# print(queue)
# queue.append(30)
# print(queue)
# queue.pop(0)
# print(queue)


class queue(list):
    def push(self, data):
        self.append(data)

    def is_empty(self):
        return len(self) == 0

    def pop(self):
        if not self.is_empty():
            return super().pop(0)
        else:
            raise IndexError("No current stack exists")

    def peek(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("No current stack exists")


s1 = queue()
s1.push(5)
s1.push(10)
s1.push(12)
s1.push(1)
print(s1.peek())
s1.pop()
print(s1.peek())
