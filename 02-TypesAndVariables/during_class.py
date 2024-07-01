'''Consider what data type the following values represent. Then check your answers (run Python in interactive mode). You can use the available type(value) function.
print(type(50))
print(type(149.17))
print(type(4*7))
print(type(1.0*7))
print(type('Krakow University of Economics'))
print(type(True))
print(type(2>5))'''


'''Write a program that calculates the sum of two integer numbers contained in variables. 
number1 = int(input('Podaj pierwsza liczbe: '))
number2 = int(input('Podaj druga liczbe: '))
print(f'number1 = {number1} \nnumber2 = {number2}')
result = number1 + number2
print(f'The result of summation: {result}')'''


'''Natural values 15, 1, 8, 6, 31 have been assigned to variables named n1, n2, n3, n4, n5. 
n1 = 15
n2 = 1
n3 = 8
n4 = 6
n5 = 31

numa = n1 + n2 + n3 + n4 + n5 
numb = pow(n1, 2) + pow(n2, 2) + pow(n3, 2) + pow(n4, 2) + pow(n5, 2)
numc = n3 / n5
numd = n3 == n4
print(f'sum = {numa}, sum of squared variables = {numb}, quotient of the variable three and five = {numc}, message = {numd}')
'''

'''Let three variables: name, age and height contain your personal data. Write a program that, using f-strings, displays the following sentence:
name = 'Julia'
age = 24
height = 173
age6 = 30

print(f'Ma name is {name}, I am {age} years old, and my height is {height} cm. In 6 years I will be {age6} years old.')
'''

'''Write a program that calculates and displays the income of a family per person. To display the results in a readable form, use f-strings
father_income = 5450
mother_income = 4920
number_of_people = 5
total = father_income + mother_income
per_person = total / number_of_people

print(f'Total income: {total} \nIncome per person: {per_person}')'''

'''Write a program that reads your name and surname from the keyboard. Store this data in two separate variables. Then, display your first and last name separated by a single space. 
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your full name is {full_name}')'''

'''
Write a program that calculates the surface area of a cube. Read the length of the side of the cube from the keyboard. Take into account that the input() function returns a string, not a number. To convert a string to a number, use the int() function. 
side = int(input('Enter cube side: '))
surface = pow(side, 3)
print(f'The surface area of a cube with side {side} is {surface}')
'''

'''

The radius of the circle has the value 5, stored in a variable. Write a program that calculates the area and circumference of the circle. 

radius = int(input('Determine radius:'))
pi = 3.14
area = pi * pow(radius, 2)
circ = 2 * pi * radius 

print(f'area = {area}\ncircumference = {circ}')
'''

