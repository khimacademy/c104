'''
5-7. 좋아하는 과일
좋아하는 과일 리스트를 만들고 서로 독립적인 if 문을 여러 개 만들어 어떤 과일이 리스트에 있는지 체크하세요.
- 좋아하는 과일 리스트를 favorite_fruits에 저장하세요.
- if 문을 다섯 개 만드세요. 각 if 문은 어떤 과일이 리스트에 있는지 체크해야 합니다. 과일이 리스트에 있다면 if 블록은 "당신은 바나나를 정말 좋아하는군요!" 같은 문장을 출력해야 합니다.

Output:
You really like blueberries!
You really like peaches!
'''

favorite_fruits = ['blueberries', 'salmonberries', 'peaches']

if 'bananas' in favorite_fruits:
    print('You really like bananas!')
if 'apples' in favorite_fruits:
    print('You really like apples!')
if 'blueberries' in favorite_fruits:
    print('You really like blueberries!')
if 'kiwis' in favorite_fruits:
    print('You really like kiwis!')
if 'peaches' in favorite_fruits:
    print('You really like peaches!')

