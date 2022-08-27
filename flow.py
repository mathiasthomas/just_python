# Boolean Values
# 1 True
# 2 False

# Comparison Operators
#  ==  Equals to 
#  != Not equal to
#  <  less than
#  > gretaer than
#  <=  less or equal to
#  >=  greater or equal to

#Booolean operators
  # Not OR And


 #ex 1 
 # mixing boolean and comparison operators
# (3>4) and (5<8)
## IF STATEMENT

# myInput = input()
# if myInput == 'thomas':
#     print('correct' + myInput)

#Example 1

# myName = 'fidelia'
# myAge = 2500
# if myName == 'fidelia':
#     print('hello welcome fidelia')
# elif myAge >100:
#     print('Hey Granny You aint in the system')


# While Loop
# the code in while clause will always ecxecute as long as the while condition  is true

# spam = 0
# while spam <5:
#     print('helloo')
#     spam = spam + 1

# name = ''
# while name != 'tom':
#     print('please enter your name')
#     name = input()
# print('thank you')
# while True:
#     print( 'Please Enter Your Name')
#     name = input()
#     if name == 'tom':
#         break
# print('thanks')

# while True:
#     print('who are you?')
#     name = input()
#     if name != 'joe':
#         continue
#     print('hello joe what is your pass3word ? ')
#     password = input()
#     if password == 'mvikia':
#         break
#     print('acces granted')


# For Loops  and Range function
#allows running of a certern block of content only for a number of times

# print('my name is ')
# for i in range(5):
#     print('tom')
# total = 0

# for i in range(101):
#     total = total+i
#     print(total)
for i in range(12, 20):
    print(i)
    #starts at 12 and ends at 20

for x in range(2 , 20 , 3):
    print(x)
    #starts at 2, ends at 20 and icrements with 3