'''
6-6. 설문
- 좋아하는 언어 설문에 참여해야 하는 사람들 리스트를 만드세요. 이름 일부는 딕셔너리에 이미 있는 이름을 쓰고, 딕셔녀리에 없는 이름도 쓰세요.
- 좋아하는 언어 설문에 참가해야 하는 사람들 리스트에 루프를 실행하세요. 이미 참여했다면 참여에 감사하는 메시지를 출력하세요. 아직 참여하지 않았다면 설문에 초대하는 메시지를 출력하세요.

Output:
jen's favorite language is python.
sarah's favorite language is c.
phil's favorite language is python.
edward's favorite language is ruby.


Thank you for taking the poll, phil!
josh, what's your favorite programming language?
david, what's your favorite programming language?
becca, what's your favorite programming language?
Thank you for taking the poll, sarah!
matt, what's your favorite programming language?
danielle, what's your favorite programming language?
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name + "'s favorite language is " + language + '.')

print('\n')

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print('Thank you for taking the poll, ' + coder + '!')
    else:
        print(coder + ", what's your favorite programming language?")

