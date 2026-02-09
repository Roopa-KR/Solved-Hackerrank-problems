from collections import deque
stack=deque()
for i in range(0,10):
    stack.append(i)
print(stack)
#To remove the last element
print(stack.pop())
print(stack)
#To remove the first element
print(stack.popleft())
print(stack)