'''
9.	A test is passed when the number of correctly completed tasks is at least 50%. Write a program that checks whether the test is passed. The total number of test tasks and the number of correctly completed tasks are included in variables. 
total_points = int(input('Enter total points: '))
gained_points = int(input('Enter gained points: '))

percent = (gained_points * 100) / total_points

if percent >= 50:
    print('Test passed')
else:
    print('Test failed')
'''

'''
10.	Write a program to calculate the absolute value of a number entered from the keyboard. 
number = int(input('Enter number: '))

if number < 0:
    new_number = number *(-1)
else:
    new_number = number 
print(f'|{number}| = {new_number}')
'''

''' 11.	Write a program that checks whether the number entered from the keyboard is even or odd. 
number = int(input('Enter number: '))
if number % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')
'''

'''12.	Write a program that checks that two people are adults. Read people’s data from the keyboard. 
first_name = input('Enter first person name: ')
first_age = int(input('Enter first person age: '))
second_name = input('Enter second person name: ')
second_age = int(input('Enter second person age: '))

if first_age >= 18 and second_age >= 18:
    print(f'Both {first_name} and {second_name} are adults')
elif first_age >= 18 and second_age < 18:
    print(f'Only {first_name} is adult')
elif first_age < 18 and second_age >= 18:
    print(f'Only {second_name} is adult')
elif first_age < 18 and second_age < 18:
    print(f'Neither {first_name} and {second_name} are adults')
'''

'''13.	A user enters two integer numbers from the keyboard. Write a program that checks whether at least one of them is not negative. 
number_one = int(input('Enter number 1: '))
number_two = int(input('Enter number 2: '))

if number_one > 0 or number_two > 0:
    print(f'At least one of entered numbers {number_one} and {number_two} is not negative')
else:
    print(f'Both numbers {number_one} and {number_two} are negative')
'''

'''
17.	Write a program that calculates the sum of integer numbers in the range <1,5>. Use the "while" statement.
sum = 0
i = 1
while i<=5:
    print(i)
    sum = sum + i
    i = i + 1
print(f'Sum is {sum}')
'''

'''
18.	Write a program that calculates values for the following fractions: 1/2, 1/3, ..., 1/10. First, Use the "while" statement, then, the "for" statement. 
i = 1
while i<=10:
    divide = 1/i
    print(f'1/{i}={divide}')
    i = i + 1


for i in range(1, 11):
    divide = 1/i
    print(f'1/{i}={divide}')
'''

'''
19.	Write a program that calculates the sum of even numbers in the range <1,10>.
sum = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum = sum + i 
print(sum)
'''

