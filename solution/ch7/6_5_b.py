'''
6-5. 강
세 가지 큰 강과 그 강이 흐르는 나라를 딕셔너리에 저장하세요. 키-값 쌍 중 하나는 'nile': 'egypt' 같은 형태가 될 겁니다.
- 루프를 써서 각 강에 대해 "나일강은 이집트에 있습니다." 같은 문장을 출력하세요.
- 루프를 써서 닥셔너리에 포함된 각 강 이름을 출력하세요.
- 루프를 써서 닥셔너리에 포함된 각 나라 이름을 출력하세요.

Output*:
The mississippi flows through united states.
The yangtze flows through china.
The fraser flows through canada.
The nile flows through egypt.
The kuskokwim flows through alaska.

The following rivers are included in this data set:
- mississippi
- yangtze
- fraser
- nile
- kuskokwim

The following countries are included in this data set:
- united states
- china
- canada
- egypt
- alaska
*Sometimes we like to think of Alaska as our own separate country.
'''

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print('The ' + river + ' flows through ' + country + '.')

print('\nThe following rivers are included in this data set:')
for river in rivers.keys():
    print('- ' + river)

print('\nThe following countries are included in this data set:')
for country in rivers.values():
    print('- ' + country)

