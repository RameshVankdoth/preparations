class SimpleHashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket

    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        print("Hash Set Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")


hash_set = SimpleHashSet(size=10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

hash_set.print_set()

print("\n'Peter' is in the set:", hash_set.contains("Peter"))
print("Removing 'Peter'")
hash_set.remove("Peter")
print("'Peter' is in the set:", hash_set.contains("Peter"))
print("'Adele' has hash code:", hash_set.hash_function("Adele"))


# MEthod 2
def first_duplicate(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
    return -1


arr = [1, 2, 3, 3, 4, 5]
print(first_duplicate(arr))


# MEthod 3
def dup(arr):
    return len(set(arr)) != len(arr)


print(dup(arr))


# MEthod 3
def two_sum(arr, target):
    hashmap = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i


print(two_sum(arr, 5))

# Update
