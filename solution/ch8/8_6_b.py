'''
8-6. 도시 이름
도시와 국가 이름을 받는 city_country() 함수를 만드세요. 이 함수는 다음과 같은 문자열을 반환해야 합니다.
'Santiago, Chile'
- 최소한 세 개의 도시-국가 쌍으로 함수를 호출하고 반환값을 출력하세요.

Output:
santiago, chile
ushuaia, argentina
longyearbyen, svalbard
'''

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city + ', ' + country)

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)

