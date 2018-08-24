'''
6-7. 사람들
연습문제 6-1의 프로그램에서 시작하세요. 서로 다른 사람을 나타내는 두 딕셔너리를 새로 만들고 딕셔녀리 세 개를 모두 people 리스트에 저장하세요. 사람들 리스트에 루프를 실행하세요. 루프 안에서 각 사람에 대해 알고 있는걸 모두 출력하세요.

Output:
eric matthes, of sitka, is 43 years old.
ever matthes, of sitka, is 5 years old.
willie matthes, of sitka, is 8 years old.
'''

# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'ever',
    'last_name': 'matthes',
    'age': 5,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 8,
    'city': 'sitka',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'] + ' ' + person['last_name']
    age = str(person['age'])
    city = person['city']
    
    print(name + ', of ' + city + ', is ' + age + ' years old.')

