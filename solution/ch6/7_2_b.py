'''
7-2. 레스토랑 예약
사용자에게 저녁 식사에 몇 명이 오는지 묻는 프로그램을 만드세요. 답이 "9명 이상이면 자리가 날 때까지 기다려야 합니다."는 메시지를 출력하세요. 그렇지 않다면 테이블이 준비됐다고 알리세요.

Output:
How many people are in your dinner party tonight? 12
I'm sorry, you'll have to wait for a table.
or:

How many people are in your dinner party tonight? 6
Your table is ready.
'''

party_size = int(input('How many people are in your dinner party tonight? '))

if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print('Your table is ready.')

