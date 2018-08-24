'''
5-6. 성장단계
if-elif-else 문을 써서 사람의 성장단계를 판단하세요. 먼저 age 변수의 값을 정하세요.
- 2살 미만이면 영아(baby)라는 메시지를 출력하세요.
- 2살 이상 4살 미만이면 유아(toddler)라는 메시지를 출력하세요.
- 4살 이상 13살 미만이면 아이(kid)라는 메시지를 출력하세요.
- 13살 이상 20살 미만이면 청소년(teenager)이라는 메시지를 출력하세요.
- 20살 이상 65살 미만이면 성인(adult)이라는 메시지를 출력하세요.
- 65살 이상이면 노인(elder)이라는 메시지를 출력하세요.

Output:
You're a teenager!
'''

age = 17

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")

