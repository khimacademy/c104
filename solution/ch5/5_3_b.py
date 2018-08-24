'''
5-3. 외계인 색 #1
게임에서 지금 막 외계인을 격추했다고 합시다. alien_color 변수를 만들고 그 값에 'green'이나 'yellow', 'red'를 할당하세요.
- 외계인 색이 녹색인지 확인하는 if 문을 만드세요. 녹색이라면 플레이어가 5점을 얻었다는 메시지를 출력하세요.
- 이 프로그램을 if 테스트가 성공하는 버전, 실패하는 버전 두 가지로 만드세요(실패하는 버전은 메시지를 출력하지 않습니다).

Output1:
You just earned 5 points!

Output2:
(no output)
'''
alien_color = 'red'
#alien_color = 'green'

if alien_color == 'green':
    print('You just earned 5 points!')

