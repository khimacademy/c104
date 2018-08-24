'''
7-9. 패스트라미 없음
연습문제 7-8의 sandwich_orders 리스트를 사용하되, 'pastrami' 샌드위치가 리스트에 최소한 세 번 나오게 하세요. 프로그램의 시작 부분 근처에 코드를 추가해 가게에 패스트라미가 다 떨어졌다는 메시지를 출력하고, while 루프를 써서 sandwich_orders의 'pastrami' 를 모두 제거하세요. finished_sandwiches에는 패스트라미 샌드위치가 없어야 합니다.

Output:
I'm sorry, we're all out of pastrami today.

I'm working on your roast beef sandwich.
I'm working on your turkey sandwich.
I'm working on your grilled cheese sandwich.
I'm working on your veggie sandwich.

I made a roast beef sandwich.
I made a turkey sandwich.
I made a grilled cheese sandwich.
I made a veggie sandwich.
'''

sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('\n')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\n')
for sandwich in finished_sandwiches:
    print('I made a ' + sandwich + ' sandwich.')

