from memory_profiler import profile


@profile
def valid(s):
    stack = []
    mapping = {"}": "{", "]": "[", ")": "("}
    for i in s:
        if i in mapping.values():
            stack.append(i)
        elif i in mapping:
            if not stack or stack[-1] != mapping[i]:
                return False
            stack.pop()
    return not stack


sample = "(]}}{][)"
print(valid(sample))

# Update
