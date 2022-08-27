#example
import random
import sys


# for i in range(5):
#     print(random.randint(0,8))


while True:
    print('type exit if you want to exit')
    res = input()
    if res == 'exit':
        sys.exit()
    print('you have typed' + res + '.' )