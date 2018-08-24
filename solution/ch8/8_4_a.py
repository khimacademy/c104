'''
8-4. L 사이즈
make_shirt() 함수를 수정해 티셔츠 사이즈 기본값을 L로, 메시지 기본값은 I love Python으로 만드세요. 기본 메시지가 새겨진 L 사이즈 셔츠, 다른 메시지가 새겨진 다른 사이즈 셔츠를 만드세요.

Output:
I'm going to make a large t-shirt.
It will say, "I love Python!"

I'm going to make a medium t-shirt.
It will say, "I love Python!"

I'm going to make a small t-shirt.
It will say, "Programmers are loopy."
'''

def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + ' t-shirt.')
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')

