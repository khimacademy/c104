'''
7-6. 세 가지 탈출구
연습문제 7-4나 연습문제 7-5의 다른 버전을 만들되, 다음 세 가지 방법을 최소한 한 번씩은 쓰세요.
- while 문 안에서 조건 테스트를 이용해 루프를 끝내세요.
- active 변수를 사용해 루프를 끝내세요.
- 사용자가 'quit' 값을 입력하면 break 문으로 루프를 빠져나가세요.

Output:
What topping would you like on your pizza?
Enter 'quit' when you are finished: ham
  I'll add ham to your pizza.

What topping would you like on your pizza?
Enter 'quit' when you are finished: quit
'''

prompt = '\nWhat topping would you like on your pizza?'
prompt += "\nEnter 'quit' when you are finished: "

active = True

while active:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + ' to your pizza.')
    else:
        active = False

