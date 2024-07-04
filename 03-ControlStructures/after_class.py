'''21.	Write a program that displays two numbers entered from the keyboard in ascending order.
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))

if first_number > second_number:
    print(f'Numbers in ascending order: {second_number}, {first_number}')
else:
    print(f'Numbers in ascending order: {first_number}, {second_number}')
'''

'''22.	Most female names in Polish end with the letter "a". Write a program that displays the name entered from the keyboard, provided it is a female name. 
name = input('Enter name: ')
if name[-1] == 'a':
    print(f'{name} - Polish female name')
else:
    print(f'{name} - Polish male name')
'''

'''23.	Write a program that calculates a dog's age in dog’s years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years
human_years = int(input('Enter the dog\'s age in human years: '))
if human_years <=2:
    dog_years = human_years * 10.5
else:
    left = human_years - 2
    dog_years = 21 + 4 * left 
print(f'The dog\'s age in dog\'s years is {dog_years} years')
'''

'''24.	A computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program displays a purchase recommendation:
current_price = float(input('Current product price: '))
previous_price = float(input('Previous product price: '))

decrease = previous_price - current_price
percent = (decrease * 100)/previous_price

if percent >= 10:
    print(f'Buy the product!\nProduct price reduced by {percent}%')
else:
    print('Not recommended')
'''

'''25.	In one of the online stores, a 25% discount is charged for each product purchased over two. Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard. number = int(input('Number of products purchased: '))
price = int(input('Product price: '))

if number > 2:
    discount = price * 0.25 
    amount = (number * price) - ((number - 2) * 0.25 * price)
else:
    amount = price * number 
    
print(f'Amount to pay: {amount}')
'''

'''26.	The speed of vehicles on highways in Poland is at least 40 km/h and not more than 140 km/h. Write a program that displays a message when the specified car speed, read from the keyboard, has been exceeded. 
car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140 

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
'''

'''27.	An influencer is a person who can influence other people's behaviour. An influencer communicates with other people using social networking sites. Write a program that checks whether a given person can be a good influencer, that is, whether the person has at least two of the following accounts: Facebook, Twitter or Instagram. Use logical type variables: facebook, twitter, instagram, the value of which indicates whether the person has an account on the social networking site. 
facebook = True
twitter = False 
instagram = True 

if (facebook and twitter) or (facebook and instagram) or (instagram and twitter):
    print('A person can be a good influencer!')
'''

'''28.	EAN-13 (European Article Number) is a barcode for marking goods. The first 3 digits (590) usually indicate goods manufactured in Poland. Write a program that checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits). Display a message if the number is correct. Additionally, only when the article number is correct, display a message when the product was manufactured in Poland. 
number = input('Enter EAN-13 article number: ')
if len(number) == 13:
    print('Article number is correct')
    if number[0] == '5' and number[1] == '9' and number[2] == '0':
        print('Article manufactured in Poland')
else:
    print('Article number is incorrect')
'''

'''29.	A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 70 minutes, and wash shoes, which takes 20 minutes. In addition, it is possible to program an additional rinse (15 minutes) and an additional spin (9 minutes). The washing machine settings are saved in variables. Write a program that calculates and displays the total washing time. 
washing_product = "shoes"
rinse = True
spin = False

if washing_product == "shoes":
    wash_time = 20
elif washing_product == "jacket":
    wash_time = 40
elif washing_product == "underwear":
    wash_time = 70
    
if rinse == True: 
    rinse_time = 15
else:
    rinse_time = 0
    
if spin == True: 
    spin_time = 9
else: 
    spin_time = 0

total = wash_time + rinse_time + spin_time

print(f'Total washing time: {total} minutes')
'''

'''30.	Write a program that allows you to convert time in 24-hour format to 12-hour format. The time in 24-hour format (hh:mm) is read from the keyboard. 
time = input('Enter time: ')
minutes = time[3] + time[4]

if time[0] == '0':
    first = time[1]
    print(f'Time in 12-hour format: {first}:{minutes}')
else:
    number = int(time[1])
    first = number - 2
    print(f'Time in 12-hour format: {first}:{minutes}pm')
'''
'''
31.	Let x and y denote the coordinates of a point on the plane. Write a program that determines in which quadrant of the coordinate system the point P (x, y) is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system. 
x = 5
y = 2

if x > 0 and y > 0:
    print(f'Point P({x}, {y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x}, {y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
        print(f'Point P({x}, {y}) is in the third quadrant of the coordinate system')
elif x > 0 and y < 0:
        print(f'Point P({x}, {y}) is in the fourth quadrant of the coordinate system')
'''

'''32.	Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs. Write a program that displays a survey consisting of three questions. Save the answers to logical type variables. Then view the survey result. 
computer = input('Are you interested in computer science (Y/N): ')
games = input('Do you like playing games (Y/N): ')
instagram = input('Do you have an Instagram account (Y/N): ')

if computer == 'Y':
    print('Interested in computer science: Yes')
elif computer == 'N':
    print('Interested in computer science: No')
else:
    print('Incorrect answer')

if games == 'Y':
    print('Interested in computer science: Yes')
elif games == 'N':
    print('Interested in computer science: No')
else:
    print('Incorrect answer')

if instagram == 'Y':
    print('Interested in computer science: Yes')
elif instagram == 'N':
    print('Interested in computer science: No')
else:
    print('Incorrect answer')
'''

'''33.	Write a program that converts a decimal number into a binary number. 
decimal = int(input('Enter decimal number: '))
binary = ""

if decimal == 0:
    binary = '0'
else:
    
    while decimal >= 1: 
        remainder = decimal % 2 
        binary = binary + str(remainder)
        decimal = int(decimal / 2)
reverse = binary[::-1]
print(f'{decimal}(10) = {reverse}(2)')
'''


'''
34.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.
amount = int(input('Enter the amount in PLN: '))

num_5 = amount // 5
amount %= 5

num_2 = amount // 2
amount %= 2

num_1 = amount

print("Minimum coins needed:")
if num_5 > 0:
    print(f"5 PLN: {num_5} coin(s)")
if num_2 > 0:
    print(f"2 PLN: {num_2} coin(s)")
if num_1 > 0:
    print(f"1 PLN: {num_1} coin(s)")
'''
'''
for i in range (1, 31):
    if  i % 5 == 0 and i % 3 == 0:
        print('THREE')
    elif i % 5 == 0:
        print('FIVE')
    elif i % 3 == 0:
        print('BINGO')
    else:
        print(i)
'''

'''
36.	Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user. 
number = int(input('Enter number: '))
for i in range (1, 10):
    print(f'{number} x {i} = {number*i}')
'''

'''
37.	Write a program that creates the following pattern
for i in range(1, 6):
    print('*'*i)

for j in range (4, 0, -1): #range(start_value, end_value, step)
    print('*'*j)
'''

'''
38.	Write a program that creates the following pattern. 
for i in range (1, 10):
    print(str(i) * i)
'''
'''
39.	The variables a and b contain the dimensions of the sides of the rectangle. Write a program that creates the following rectangle with dimensions a and b. Sample result for a = 4 and b = 15:
a = 4
b = 15 



for i in range(a):
    
    if i == 0 or i == a-1:
        
        for j in range(b):
            
            print('*', end='') 

    print('*' + ' '*(b-1) + '*')
        
'''

'''
40.	The 'university' variable contains the name of university where you are studying. Write a program that displays the contents of the variable with an extra space between characters (add a space between each character). 
university = 'Krakow University of Economics'

for i in range(30):
    print(university[i] + ' ', end='')
'''

'''
41.	The payment card is secured with a four-digit PIN code (0805). Write a program that checks if the PIN code entered in the payment terminal is correct. The user has up to three possibilities for entering a PIN code. In case of three unsuccessful attempts, the card is blocked. Sample 

code = input('Enter the PIN code: ')
pin = '0805'

if code[0] != pin[0] or code[1] != pin[1] or code[2] != pin[2] or code[3] != pin[3]:
    for i in range(2):
        if code[0] != pin[0] or code[1] != pin[1] or code[2] != pin[2] or code[3] != pin[3]:
            print('Incorrect..')
            code = input('Enter the PIN code: ')
    print('Sorry, your payment card has been blocked')
'''

'''
42.	A computer numeric keyboard has the arrangement of the keys as below. The included program code displays the computer keyboard. Analyse the program in terms of the displayed results. Do you understand each program statement? Then make a change in your program code. Replace the ‘for’ with a ‘while’ statement.

i = 6
while i >= 0:
    j = 1
    while j < 4:
        print(f' {i+j}', end='')
        j += 1
    print()
    i -= 3
'''

'''
43.	Write a program that displays the first twenty words of the Fibonacci sequence. The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two. 
a = 1
b = 1
print('term 0 / number: 0')
print('term 1 / number: 1')
print('term 2 / number: 1')

for term in range (3,21):
    c = a + b
    print(f'term: {term} / number: {c}')
    a = b
    b = c
'''

'''
44.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. Entering 0 ends entering numbers. 
number = int(input('Enter number: '))
count = 0
sum = number 
while number != 0:
    number = int(input('Enter number: '))
    count = count + 1
    sum = sum + number 

mean = int(sum / count)
print(f'RESULT: Quantity = {count}, Sum = {sum}, Mean = {mean}')
'''

'''
45.	A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. Write a program that finds N leading prime numbers. Read the value of N from the keyboard. Using loop statements check that the number N is divisible only by 1 and by N.
# Number of prime numbers to find
N = 10

# Initialize variables
count = 0  # To count the number of primes found
num = 2    # The current number to be checked for primality

# Loop to find and print the first 10 prime numbers
while count < N:
    is_prime = True

    # Check if the current number is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # If the number is prime, print it and increment the count
    if is_prime:
        print(num, end=' ')
        count += 1

    # Move to the next number
    num += 1
'''

'''
46.	Write a program that displays a lottery coupon (numbers from 1 to 49) in the format as below.

# Initialize the maximum number and the number of columns
max_num = 49
cols = 7

# Loop to generate and print the numbers in the specified format
for row in range(1, cols + 1):
    for col in range(row, max_num + 1, cols):
        print(f"{col:2}", end=' ')
    print()
'''

'''
47.	Write a program that displays 20 integer random numbers in the range of 5 to 10.


import random

# Generate and print 20 random integers in the range of 5 to 10
for _ in range(20):
    random_integer = random.randint(5, 10)
    print(random_integer, end=' ')
'''

