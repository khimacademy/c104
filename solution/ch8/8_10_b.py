'''
8-10. 훌륭한 마술사
연습문제 8-9의 프로그램을 복사해서 시작하세요. 각 마술사 이름에 '훌륭한'이라는 구절을 붙여서 마술사 리스트를 수정하는 make_great() 함수를 만드세요. show_magicians()를 호출해서 리스트가 실제 수정됐는지 확인하세요.

Output:
harry houdini
david blaine
teller

teller the Great
david blaine the Great
harry houdini the Great
'''

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

print('\n')
make_great(magicians)
show_magicians(magicians)

