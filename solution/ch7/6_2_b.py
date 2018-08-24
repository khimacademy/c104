'''
6-2. 좋아하는 숫자
사람들이 좋아하는 숫자를 딕셔너리에 저장하세요. 다섯 명의 이름을 생각 하고 그 이름을 딕셔너리 키로 쓰세요. 각 사람이 좋아하는 숫자를 생각하고 그 숫자를 딕셔너리 값으로 쓰세요. 각 사람 이름과 좋아하는 숫자를 출력하세요. 더 재미있게 하고 싶으면 실제 친구에게 좋아하는 숫자를 물어보고 프로그램 데이터로 쓰세요.

Output:
Mandy's favorite number is 42.
Micah's favorite number is 23.
Gus's favorite number is 7.
Hank's favorite number is 1000000.
Maggie's favorite number is 0.
'''

favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000000,
    'maggie': 0,
    }

num = favorite_numbers['mandy']
print("Mandy's favorite number is " + str(num) + '.')

num = favorite_numbers['micah']
print("Micah's favorite number is " + str(num) + '.')

num = favorite_numbers['gus']
print("Gus's favorite number is " + str(num) + '.')

num = favorite_numbers['hank']
print("Hank's favorite number is " + str(num) + '.')

num = favorite_numbers['maggie']
print("Maggie's favorite number is " + str(num) + '.')

