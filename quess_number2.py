import random
secretNumber = random.randint(1, 15)
# print('This is my secret number' + str(secretNumber))
print('Think of a secret number and enter it below')

for numberofQuesses in range(1,5):
    quess = int(input())

    if quess < secretNumber:
        print(' Sorry the number you entered is too low')

    elif quess > secretNumber:
         print(' Sorry the number you entered is too high')
    else:
        break
if quess == secretNumber:
    print('Congratulations you chose the correct number in ' + str(numberofQuesses) + 'times')

else:
    print('sorry you failed')

