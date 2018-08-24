'''
5-10. 사용자 이름 체크
다음과 같이 프로그램을 만들어 웹사이트에서 모든 사용자가 고유한 사용자 이름을 쓰는지 확인하세요.
- 사용자 이름을 다섯 개 이상 만들고 current_users 리스트에 저장하세요.
- 다른 사용자 이름 다섯 개를 new_users 리스트에 저장하세요. 새 사용자 이름 중 한두 개는 current_users 리스트에 이미 있는 이름을 쓰세요.
- new_users 리스트에 루프를 실행해 새 사용자 이름이 이미 사용 중인지 확인하세요. 이미 사용 중이라면 다른 사용자 이름이 필요하다는 메시지를 출력하세요 사용 중이 아니라면 사용자 이름을 쓸 수 있다는 메시지를 출력하세요.
- 비교할 때는 대소문자를 구분하지 마세요. 'John'이 이미 사용 중이라면 'JOHN'은 안 됩니다.

Output:
Great, sarah is still available.
Sorry Willie, that name is taken.
Great, PHIL is still available.
Sorry ever, that name is taken.
Great, Iona is still available.
Note: If you're not comfortable with list comprehensions yet, the list current_users_lower can be generated using a loop:

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
'''

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('Sorry ' + new_user + ', that name is taken.')
    else:
        print('Great, ' + new_user + ' is still available.')

