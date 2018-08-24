'''
8-2. 좋아하는 책
매개변수로 title 하나를 받는 함수 favorite_book()을 만드세요. 이 함수는 "내가 좋아하는 책은 이상한 나라의 앨리스입니다." 같은 메시지를 출력해야 합니다. 함수를 호출하고 책 제목을 매개변수로 전달하세요.

Output:
The Abstract Wild is one of my favorite books.
'''

def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + ' is one of my favorite books.')

favorite_book('The Abstract Wild')

