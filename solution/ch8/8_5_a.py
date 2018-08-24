'''
8-5. 도시
도시 이름과 나라 이름을 받는 describe_city() 함수를 만드세요. 이 함수는 "레이캬비크는 아이슬랜드에 있습니다." 같은 단순한 문장을 출력해야 합니다. 나라 이름 매개변수에 기본값을 지정하세요. 세 개의 도시에 대해 함수를 호출하되, 최소한 하나는 기본값인 나라에 있지 않은 도시를 써야 합니다.

Output:
santiago is in chile.
reykjavik is in iceland.
punta arenas is in chile.
'''

def describe_city(city, country='chile'):
    """Describe a city."""
    msg = city + ' is in ' + country + '.'
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')

