def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pairs[char]:
                return "Not Balanced"
            stack.pop()

    if not stack:
        return "Balanced"
    else:
        return "Not Balanced"


expr1 = "(a+b)*(c+d)"
expr2 = "(a+b)*(c+d"

print("Input:", expr1)
print("Output:", is_balanced(expr1))

print("Input:", expr2)
print("Output:", is_balanced(expr2))