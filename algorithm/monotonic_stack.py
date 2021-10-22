'''

Ascending: the top of stack always largest
Descending: the top of stack always smallest
'''

# find the next greater
array = [1,6,0,2,8,3]
stack = [] # desc 

table = {} # num : next greater num
for num in array:
    
    while stack and stack[-1] < num:
        top = stack.pop()
        table[top] = num
    stack.append(num)

print("the greater", table)

# find the next less eqaul
array_lesser = [5,8,3,7,7,10,6]
stack = [] # asc

table = {} # {number index : next lesser number index}
for i, num in enumerate(array_lesser):
    print(stack)
    while stack and array_lesser[stack[-1]] >= num:
        top = stack.pop()
        table[top] = i
    stack.append(i)

for idx in table:
    lesser_idx = table[idx]
    print(f"num: {array_lesser[idx]} next lesser num is {array_lesser[lesser_idx]}")