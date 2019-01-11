import time
import random

print('I am rock, paper, scissors Bot!')
time.sleep(0.7)
user = input('Choose your fighter! ')
time.sleep(0.7)
print('Rock!')
time.sleep(0.7)
print('Paper!')
time.sleep(0.7)
print('Scissors!')
time.sleep(0.7)
print('Say Shoot!')


comp = random.randint(1,3)

if comp == 1:
	comp = 'Rock'
	time.sleep(0.7)
	print('Rock')
elif comp == 2:
	comp = 'Paper'
	time.sleep(0.7)
	print('Paper')
else:
	comp = 'Scissors'
	time.sleep(0.7)
	print('Scissors')

if user == 'Rock' and comp == 'Rock':
	print('Lets run that back.')
elif user == 'Rock' and comp == 'Paper':
	print('Ha, I win!')
elif user == 'Rock' and comp == 'Scissors':
	print('Shiet, you win')
elif user == 'Paper' and comp == 'Paper':
	print('Lets run that back.')
elif user == 'Paper' and comp == 'Rock':
	print('Shiet, you win.')
elif user == 'Paper' and comp == 'Scissors':
	print('Ha, I win!')
elif user == 'Scissors' and comp == 'Paper':
	print('Shiet, you win.')
elif user == 'Scissors' and comp == 'Rock':
	print('Ha, I win!')
elif user == "Scissors" and comp == 'Scissors':
	print('Lets run that back.')
elif user == 'rock' and comp == 'Rock':
	print('Lets run that back.')
elif user == 'rock' and comp == 'Paper':
	print('Ha, I win!')
elif user == 'rock' and comp == 'Scissors':
	print('Shiet, you win.')
elif user == 'paper' and comp == 'Paper':
	print('Lets run that back.')
elif user == 'paper' and comp == 'Rock':
	print('Shiet, you win.')
elif user == 'paper' and comp == 'Scissors':
	print('Ha, I win!')
elif user == 'scissors' and comp == 'Paper':
	print('Shiet, you win.')
elif user == 'scissors' and comp == 'Rock':
	print('Ha, I win!')
elif user == 'scissors' and comp == 'Scissors':
	print('Lets run that back.')
else:
	print('Lets run that back.')