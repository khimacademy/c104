'''
6-10. 좋아하는 숫자
연습문제 6-2의 프로그램을 수정해서 각 사람이 좋아하는 숫자를 두 개 이상 택할 수 있게 하세요. 각 사람 이름과 그들이 좋아하는 숫자를 함께 출력하세요.

Output:
micah likes the following numbers:
  42
  39
  56

mandy likes the following numbers:
  42
  17

gus likes the following numbers:
  7
  12
'''

favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print('\n' + name + ' likes the following numbers:')
    for number in numbers:
        print('  ' + str(number))

