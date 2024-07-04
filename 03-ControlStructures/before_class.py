'''
# Example of a for loop in Python
for i in range(5):  # This will iterate 5 times (i will take values 0, 1, 2, 3, 4)
    print(f"Iteration {i+1}: Hello, world!")
    '''


'''# Example of a while loop in Python
count = 0
while count < 5:  # This loop will continue as long as count is less than 5
    print(f"Iteration {count+1}: Hello, world!")
    count += 1  # Increment count by 1 in each iteration
    '''
    
'''
for x in range(2):
    for y in range(3):
        print(f'({x}, {y})')
'''
        
'''
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'We have {count} even numbers')
'''

sum = 0
number = 1
while number <= 5:
  sum = sum + number
  number = number + 1
message = print(f"Sum of numbers in <1,5> is {sum}")
print(message)
