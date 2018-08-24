'''
5-2. 더 많은 조건 테스트
꼭 열 가지만 테스트하란 법은 없습니다. 더 많이 비교하고 싶다면 테스트를 더 만들어 보세요. 다음 테스트 종류의 각 하나씩에 True와 False가 최소한 하나씩은 나와야 합니다.
- 문자열의 일치와 불일치 테스트
- 일치와 불일치, 더 큰, 더 작은, 크거나 같은, 작거나 같은 등을 포함하는 숫자형 테스트
- and와 or 키워드를 사용하는 테스트
- 항목이 리스트에 있는지 확인하는 테스트
- 항목이 리스트에 없는지 확인하는 테스트

Output:
car == 'kia'? True
car == 'bmw'? False
num > 4? True
num <= 3? False
True and False? False
True or False? True
4 in nums? True
0 in nums? False
4 not in nums? False
0 not in nums? True
'''

car = 'kia'
print("car == 'kia'?", car == 'kia')
print("car == 'bmw'?", car == 'bmw')

num = 5
print('num > 4?', num > 4)
print('num <= 3?', num <= 3)

print('True and False?', True and False)
print('True or False?', True or False)

nums = [1, 2, 3, 4, 5]
print('4 in nums?', 4 in nums)
print('0 in nums?', 0 in nums)
print('4 not in nums?', 4 not in nums)
print('0 not in nums?', 0 not in nums)

