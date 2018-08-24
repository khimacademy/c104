'''
6-4. 용어사전 2
이제 딕셔너리에 루프를 실행하는 방법을 잘 알게 됐으니 연습문제 6-3의 코드에서 여러 번 사용한 print 문 대신 딕셔너리의 키와 값에 루프를 실행하세요.
- 루프가 잘 실행된다고 확신하면 파이썬 용어를 용어 사전에 다섯 개 추가하세요. 프로그램을 다시 실행하면 이들 새 단어와 의미가 자동으로 출력에 포함돼야 합니다.

Output:
dictionary: A collection of key-value pairs.
string: A series of characters.
boolean expression: An expression that evaluates to True or False.
comment: A note in a program that the Python interpreter ignores.
value: An item associated with a key in a dictionary.
loop: Work through a collection of items, one at a time.
list: A collection of items in a particular order.
conditional test: A comparison between two values.
key: The first item in a key-value pair in a dictionary.
float: A numerical value with a decimal component.
'''

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(word + ': ' + definition)

