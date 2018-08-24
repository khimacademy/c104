'''
6-9. 좋아하는 장소
favorite_places 딕셔너리를 만드세요. 딕셔너리 키로 쓸 이름을 세 개 생각하고 각 사람마다 좋아하는 장소를 1~3개 저장하세요. 이 연습문제를 조금 더 흥미롭게 만들려면 친구에게 좋아하는 장소 이름을 물어보세요. 딕셔너리에 루프를 실행하고 각 사람 이름과 좋아하는 장소를 출력하세요.

Output:
ever likes the following places:
- mt. verstovia
- the playground
- south carolina

erin likes the following places:
- hawaii
- iceland

eric likes the following places:
- bear mountain
- death valley
- tierra del Fuego
'''

favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
    }

for name, places in favorite_places.items():
    print('\n' + name + ' likes the following places:')
    for place in places:
        print('- ' + place)

