def isValid(s):
    stack = []
    hashmap = {')': '(', ']': '[', '}': '{'}

    for char in s:

        # If it is a closing bracket
        if char in hashmap:

            # Check if stack is empty or top doesn't match
            if not stack or stack[-1] != hashmap[char]:
                return False

            # Remove matching opening bracket
            stack.pop()

        # Opening bracket
        else:
            stack.append(char)

    # If stack is empty, all brackets matched
    return len(stack) == 0


# Input
s = input("Enter input: ")

# Output
print(isValid(s))