'''
8-3. 티셔츠
티셔츠 사이즈와 티셔츠에 출력할 메시지를 받는 make_shirt() 함수를 만드세요. 이 함수는 티셔츠 사이즈와 티셔츠에 출력할 메시지를 요약하는 문장을 출력해야 합니다. 위치형 매개변수를 사용해 함수를 한 번 호출하세요. 두 번째는 키워드 매개변수를 사용해 호출하세요.

Output:
I'm going to make a large t-shirt.
It will say, "I love Python!"

I'm going to make a medium t-shirt.
It will say, "Readability counts."
'''

def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love Python!')
make_shirt(message='Readability counts.', size='medium')

