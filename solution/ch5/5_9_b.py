'''
5-9. 사용자 없음
연습문제 5-8에 if 테스트를 추가해 사용자 리스트가 비어 있지 않음을 확인하세요.
- 리스트가 비어 있으면 "사용자가 있어야 합니다!"와 같은 메시지를 출력하세요.
- 리스트에서 사용자 이름을 모두 제거하고 정확한 메시지가 출력되는지 확인하세요.

Output:
We need to find some users!
'''

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + username + ', thank you for logging in again!')
else:
    print('We need to find some users!')

