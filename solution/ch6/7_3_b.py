'''
7-3. 10의 배수
사용자에게 숫자를 입력받고 그 숫자가 10의 배수인지 아닌지 보고하세요.

Output:
Give me a number, please: 23
23 is not a multiple of 10.
or:

Give me a number, please: 90
90 is a multiple of 10.
'''

number = int(input('Give me a number, please: '))

if number % 10 == 0:
    print(str(number) + ' is a multiple of 10.')
else:
    print(str(number) + ' is not a multiple of 10.')

