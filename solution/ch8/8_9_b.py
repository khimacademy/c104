'''
8-9. 마술사 b 
마술사 이름으로 리스트를 만들어보세요. 리스트에 있는 각 마술사 이름을 출력하는 show_magicians() 함수에 리스트를 넘기세요.

Output:
harry houdini
david blaine
teller
'''

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

