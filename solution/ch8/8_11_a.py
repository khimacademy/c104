'''
8-11. 변하지 않은 마술사
연습문제 8-10으로 시작하세요. 마술사 이름 리스트의 사본으로 make_great() 함수를 호출하세요. 원래 리스트가 바뀌지 않았으므로 반환된 새 리스트를 별도의 리스트에 저장하세요. 각 리스트에서 show_magicians()를 호출해 원래 이름이 담긴 리스트와 각 마술사 이름에 '훌륭한'이 추가된 리스트 두 가지가 있음을 확인하세요.

Output:
harry houdini
david blaine
teller

Great magicians:
teller the Great
david blaine the Great
harry houdini the Great

Original magicians:
harry houdini
david blaine
teller
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

    return magicians

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

print('\nGreat magicians:')
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print('\nOriginal magicians:')
show_magicians(magicians)

