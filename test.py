dict = {
    ")": "(",
    "}": "{",
    "]": "["
}

stack = []

for key in dict.keys():
    stack.append(key)
print(stack)