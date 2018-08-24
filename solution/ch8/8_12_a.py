'''
8-12. 샌드위치
고객이 샌드위치에 넣고 싶어하는 재료 리스트를 받는 함수를 만드세요. 이 함수에는 함수 호출에서 제공하는 항목을 모두 수집하는 매개변수가 있어야 하고 주문받은 샌드위치를 요약해서 출력해야 합니다. 함수를 세 번 호출하고 그 때마다 다른 숫자의 매개변수를 넘기세요.

Output:
I'll make you a great sandwich:
  ...adding roast beef to your sandwich.
  ...adding cheddar cheese to your sandwich.
  ...adding lettuce to your sandwich.
  ...adding honey dijon to your sandwich.
Your sandwich is ready!

I'll make you a great sandwich:
  ...adding turkey to your sandwich.
  ...adding apple slices to your sandwich.
  ...adding honey mustard to your sandwich.
Your sandwich is ready!

I'll make you a great sandwich:
  ...adding peanut butter to your sandwich.
  ...adding strawberry jam to your sandwich.
Your sandwich is ready!
'''

def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print('  ...adding ' + item + ' to your sandwich.')
    print('Your sandwich is ready!')

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

