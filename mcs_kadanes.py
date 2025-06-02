from flask import Flask, jsonify

app = Flask(__name__)

with app.app_context():
    response = jsonify({"Ramesh": "name"})
    print(response.get_data(as_text=True))


a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]

print(sum(a))


def kadanes(arr):
    a = b = arr[0]
    for i in arr[1:]:
        b = max(b, b + i)
        a = max(a, b)
    return a


print(kadanes(a) - 1)


a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print(sum(a))


def kadanes(a):
    max_so_far = a[0]
    curr_max = a[0]
    size = len(a)
    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


print(kadanes(a))
