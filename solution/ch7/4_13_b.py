'''
4-13. 뷔페
뷔페 스타일의 음식점이 있는데 기본 음식은 다섯 가지밖에 없습니다. 단순한 음식 다섯 가지를 생각하고 튜플로 저장하세요.
- for 루프를 써서 이 식당의 각 음식을 출력하세요.
- 항목 중 하나를 수정하는 시도를 해보고 파이썬에서 변경을 거부하는지 확인하세요.
- 식당에서 메뉴를 교체하려 합니다. 항목 중 두 개를 다른 음식으로 바꾸세요. 튜플을 덮어쓰는 코드 블록을 추가하고, for 루프를 써서 바뀐 메뉴의 각 항목을 출력하세요.

Output:
You can choose from the following menu items:
- rockfish sandwich
- halibut nuggets
- smoked salmon chowder
- salmon burger
- crab cakes

Our menu has been updated.
You can now choose from the following items:
- rockfish sandwich
- halibut nuggets
- smoked salmon chowder
- black cod tips
- king crab legs
'''

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print('You can choose from the following menu items:')
for item in menu_items:
    print('- ' + item)

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print('\nOur menu has been updated.')
print('You can now choose from the following items:')
for item in menu_items:
    print('- ' + item)

