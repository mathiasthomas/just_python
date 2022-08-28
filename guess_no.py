import random
secretNumber = random.randint(1,20)
print('Im thinking of number between 1 and 20')
#ask the player to quess six times
for quesesTaken in range(1,7):
    print('take a quess')
    quess = int(input())
    if quess < secretNumber:
        print('quess is too low')
    elif quess > secretNumber:
        print('quess is too high')
    else:
        break

if quess == secretNumber:
    print('Good job you have quessed my number in ' + str(quesesTaken)+ 'quesses')
else:
    print('nope the number i was thinking was ' + str(secretNumber))