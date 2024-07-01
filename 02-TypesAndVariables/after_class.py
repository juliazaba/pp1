'''

Evaluate the following expressions. First, try to do it without using a computer. Then, check the results on your computer (run Python in interactive mode). 

numa = 15 * 38
numb = (3+4) * (5*9)
numc = int(7/2)
numd = int(48 % 5)
nume = (8+7+4+2)/4
numf = pow(2, 10)
numg = 49**(1/2)
numh = 80 * (1/4)

print(f'{numa}\n{numb}\n{numc}\n{numd}\n{nume}\n{numf}\n{numg}\n{numh}')
'''

'''
17.	Calculate values of the following expressions. First, try to do it without using a computer. Then, check the results on your computer (run Python in interactive mode).
numa = 5 + 10 * 5
numb = 3 - 2 + 1
numc = 2+ -3
numd = 2 ** 8
nume = 4 + 4 / 2 ** 2
numf = 4 % 3 % 2 % 1
numg = 1 + 2 % 3 ** 4 * 5
numh = True != False
numi = 2 <=3 or False 
numj = not True or not False and not True 
numk = 2 < 3 and 4 < 5 or not 6 < 7
numl = 2 % 3 < 4 / 5 and 6 + 7 < 8 or not 9 + 10 == 19
numm = 0x11 + 0b11 + 11

print(f'{numa}\n{numb}\n{numc}\n{numd}\n{nume}\n{numf}\n{numg}\n{numh}\n{numi}\n{numj}\n{numk}\n{numl}\n{numm}')'''

'''
18.	A variable x has a value of 7 and a variable y has a value of 34. Write a program that swaps variable values (x should be 34 and y should be 7). You can use one additional, auxiliary variable. 
x = 7
y = 34

print(f'Value of x: {x}\nValue of y: {y}')

temp = x
x = y 
y = temp 

print(f'Value of x after swapping: {x}\nValue of y after swapping: {y}')
'''

'''
The length of the side of the cube is contained in the variable a. Write a program that calculates and displays the volume and surface area of the cube. 
side = int(input('Cube side: '))
volume = pow(side, 3)
surface = pow(side, 2) * 6
print(f'Cube volume: {volume}\nCube surface area: {surface}')

'''
'''
Variables a and b contain two integer numbers. Write a program that calculates and displays the result of their division, rounded down to the nearest whole number. Display also the remainder of the division
one = int(input('Number one: '))
two = int(input('Number two: '))
division = int(one/two)
remainder = one % two 
print(f'Division result: {division}\nRemainder: {remainder}')
'''

'''
A variable contains your height in cm. Write a program that displays your height both in cm and in feet and inches
height = int(input('Enter height in cm: '))
feet = int(height/30.48)
remaining = height - (feet * 30.48)
inches = int(remaining * 0.3937)

print(f'I am {height}cm tall, i.e. {feet} feet and {inches} inches')
'''
'''
22.	The variables a and b contain two integers, 3 and 5, respectively. Write a program that displays the following expression containing the values of these variables and the value of the expression.
a = 3
b = 5
print(f'{a} - {b} = {a-b}')'''

'''
23.	The length of the sides of the triangle is a, b and c. Write a program that calculates the area of the triangle (using the Heron formula) and the triangle circumference. Read the values of the triangle sides from the keyboard. 
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
s = (a+b+c)/2
formula = s * (s-a) * (s-b) * (s-c)
area = int(pow(formula, (1/2)))
circumference = a + b + c
print(f'Triangle area: {area}\nTriangle circumference: {circumference}')
'''

'''
24.	Vehicle registration numbers in Kraków start with the letters KR or KK. Write a program that checks whether the vehicle registration number entered from the keyboard means a vehicle from Krakow. Display True whether a car is from Kraków or False otherwise. 
a = input('Enter vehicle registration number: ')

if a[0] == 'K' and (a[1] == 'R' or a[1] == 'K'):
    print(f'Car from Krakow: True')
else:
    print(f'Car from Krakow: False')
    
    '''
    
'''
25.	People up to and including 26 years of age are exempt from paying taxes in Poland. Write a program that, based on the person's age entered from the keyboard, displays True if the person is exempt from paying taxes and displays False otherwise. 
age = int(input('Enter age: '))
print(f'Exemption from paying taxes: {age<=26}')
'''

'''
26.	Write a program that checks whether the number entered from the keyboard is even. Display True when the number is even and False when the number is odd. 
number = int(input('Enter number: '))
print(f'Number is even: {number%2 == 0}')
'''

'''
27.	Write a program that checks whether the number entered from the keyboard is between -10 and 10. Display True if the number is in the given range, and False otherwise
number = int(input('Enter number: '))
print(f'Number in the range <-10,10>: {-10<number and number<10}')
'''
'''
28.	Correct body weight has a significant impact on health. Write a program that calculates the Body Mass Index (BMI) based on your height in cm and weight in kg. A user enters data from the keyboard. Find the formula on the Internet for calculating the BMI. Then, using your program, check that you have the correct weight. Display the calculated BMI and display True if the weight is within the valid range, or display False otherwise. 
height = int(input('Enter height in cm: '))
weight = int(input('Enter wight in kg: '))
BMI = weight / pow((height)/100, 2)
print(BMI)
print(f'Correct weight: {18.5 < BMI and 24.9 > BMI}')
'''

'''
29.	Each programming language provides a set of functions that you can use in your programs. One of them is a function that returns a random number. Write a program that displays results of three dice rolls and the sum of dice rolled. Apply a random number generator:
import random 
list = [1, 2, 3, 4, 5, 6]
a = int(random.choice(list))
b = int(random.choice(list))
c = int(random.choice(list))
sum = a + b + c
print(f'{a}\n{b}\n{c}\nsum = {sum}')

'''

'''
30.	In many games, the numbers one and six on dice have special meaning. Write a program that displays the number of dice rolled and the value True if the number rolled is 1 or 6. 
import random
list = [1, 2, 3, 4, 5, 6]
a = int(random.choice(list))
print(f'Dice rolled: {a}\nSpecial number: {a==1 or a==6}')
'''

'''
31.	Write a program that enables a user to challenge a computer. The computer throws dice. Then, the user then tries to guess the number from dice by entering a number from 1 to 6 from the keyboard. If the user has guessed the number from the dice, the computer displays True. Otherwise, the computer displays False.
import random
list = [1, 2, 3, 4, 5, 6]
a = int(random.choice(list))
b = int(input('Guess the number: '))
print(f'Guessed number: {a==b}')
'''

'''
32.	23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. Then, it calculates and displays both the amount and its VAT. Apply formatting with two decimal places
amount = float(input('Amount: '))
vat = (23 * amount) / 100
rounded_vat = round(vat, 2)
print(f'VAT 23%: {rounded_vat}')
'''
'''
33.	The password is valid if it is at least 8 characters long. Write a program that checks whether the password read from the keyboard is correct. 
a = input('Enter password: ')
print(f'Password is valid: {len(a)>=8}')
'''

'''
34.	The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. Write a program that checks whether the vehicle speed entered from the keyboard is correct. 
speed = int(input('Enter vehicle speed: '))
print(f'Speed is valid: {speed >= 40 and speed <= 140}')
'''
'''
35.	A tree may be cut down if its diameter is at least 50 cm. Write a program that, based on the circumference of the tree entered from the keyboard, calculates and displays the value True if the tree can be cut down, or display the value False otherwise. 
circ = int(input('Enter tree circumference: '))
diameter = circ / 3.14
print(f'Tree can be cut down: {diameter >= 50}')
'''

'''
36.	A bank buys and sells Euro. Write a program that, based on the Euro buying and selling rates entered from the keyboard, calculates the difference between the buying and selling rates (spread). Display result with 4 decimal places. 
buy = float(input('Bank buys EUR: '))
sell = float(input('Bank sells EUR: '))
spread = sell - buy
print(f'Spread: {round(spread, 4)}')
'''

'''
Display the employee's name, surname, initials and date of birth on separate lines
personal_data = 'Mr. John May, born on 1998-02-16'
print(f'Description: {personal_data}')
print(f'Name: {personal_data[4:8]}')
print(f'Surname: {personal_data[9:12]}')
print(f'Initials: {personal_data[4]}{personal_data[9]}')
print(f'Born: {personal_data[22:]}')
'''
'''
38.	To improve readability, telephone numbers are often presented with a dash or space separating some digits. Write a program that displays a 9-digit telephone number entered from the keyboard as three groups of 3 digits each, separated by a dash character. 
number = input('Enter phone number: ')
print(f'Phone number: {number[:3]}-{number[3:6]}-{number[6:]}')
'''

'''
39.	The price of the product on the price tag is given before and after the discount is applied. Write a program that allows you to enter the product price and discount. Display the product price, discount, discounted product price, and the difference between the product price before and after the discount. Display all prices with two decimal places. 
price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
with_discount = price - (discount * price) / 100
reduction = (discount * price) / 100
print(f'Price with discount: {round(with_discount, 2)}')
print(f'Reduction: {round(reduction, 2)}')
'''
'''
40.	The credit card number consists of 16 digits. Write a program that allows you to enter a credit card number from the keyboard. Display the credit card number in groups of 4 digits, separating the groups with a space character. 
number = input('Enter credit card number: ')
print(f'Card number: {number[:4]} {number[4:8]} {number[8:12]} {number[12:]}')
'''
'''
41.	The binary numeral system is a positional numeral system that requires only two digits to write numbers: 0 and 1. The hexadecimal numeral system is a positional numeral system that uses sixteen distinct symbols, most often the symbols "0"–"9" to represent values 0 to 9, and "A"–"F" (or alternatively "a"–"f") to represent values from ten to fifteen. Both are widely used in mathematics, computer science and digital electronics. Write a program that reads an integer number from the keyboard and displays that value as a binary and hexadecimal number. To convert a decimal number to binary or hexadecimal value, use the available Python functions
dec = int(input('Enter number: '))
print(f'Binary number: {bin(dec)}')
print(f'Hexadecimal number: {hex(dec)}')
'''
'''
42.	Write a program that allows you to enter a binary, four-digit number. Convert the entered number from binary to decimal value. Do not use available Python functions. 
binary = input('Enter a binary number: ')
if binary[0] == '1': 
    a = 8
else:
    a = 0
    
if binary[1] == '1':
    b = 4
else:
    b = 0
    
if binary[2] == '1':
    c = 2
else: 
    c = 0
    
if binary[3] == '1':
    d = 1
else: 
    d = 0
    
decimal = a + b + c + d 

print(f'Binary number in decimal notation: {decimal}')
'''
'''
43.	In computer science, every written (graphic) character of human language (letters, digits, symbols, etc.) is encoded by assigning it a number. This allows characters to be stored, transmitted, and transformed using digital computers. Write a program that displays a numerical representation of each letter of your name. To convert a character to its numerical representation, use the Python ord() function. 
name = input('Name: ')
for char in name:
    print(f"'{char}': {ord(char)}")'''