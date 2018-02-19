# a simple coin toss that must be debugged!

# that was too easy...
import random 


guess  = ''
while 1:
	guess  = ''
	print('Guess the coint toss! Enter heads or tails: ')
	guess = input()
	toss = random.randint(0,1)
	if toss and guess in (1, 'heads'):
		print('You got it!')
		break
	elif toss and guess in (0, 'tails'):
		print('You got it!')
		break
	elif guess not in ('heads', 'tails'):
		print('Try entering a valid input...\n')
		continue
	else:
		print('Try again next time!\n')
		continue
