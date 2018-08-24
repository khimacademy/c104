'''
7-8. 제과점
sandwich_orders 리스트를 만들고 다양한 샌드위치 이름을 저장하세요. 빈 리스트 finished_sandwiches를 만드세요. 샌드위치 주문 리스트에 루프를 실행해 각 주문에 대해 "참치 샌드위치를 만들었습니다." 같은 메시지를 출력하세요. 각 샌드위치가 만들어지면 완성된 샌드위치 리스트로 옮기세요. 모든 샌드위치를 다 만들면 각 샌드위치를 나열하는 메시지를 출력하세요.

Output:
I'm working on your roast beef sandwich.
I'm working on your turkey sandwich.
I'm working on your grilled cheese sandwich.
I'm working on your veggie sandwich.

I made a roast beef sandwich.
I made a turkey sandwich.
I made a grilled cheese sandwich.
I made a veggie sandwich.
'''

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + ' sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\n')
for sandwich in finished_sandwiches:
    print('I made a ' + sandwich + ' sandwich.')

