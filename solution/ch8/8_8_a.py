'''
8-8. 사용자 앨범
연습문제 8-7의 프로그램에서 시작하세요. while 루프를 만들어 사용자가 앨범 음악가와 제목을 입력하게 하세요. 정보를 받았으면 사용자가 입력한 내용을 전달하면서 make_album()을 호출하고 만들어진 닥셔너리를 출력하세요. while 루프에 종료 값을 쓰는 걸 잊지 마세요.

Output:
Enter 'quit' at any time to stop.

What album are you thinking of? number of the beast
Who's the artist? iron maiden
{'artist': 'iron maiden', 'title': 'number of the beast'}

What album are you thinking of? touch of class
Who's the artist? angel romero
{'artist': 'angel romero', 'title': 'touch of class'}

What album are you thinking of? rust in peace
Who's the artist? megadeth
{'artist': 'megadeth', 'title': 'rust in peace'}

What album are you thinking of? quit

Thanks for responding!
'''

def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist,
        'title': title,
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = '\nWhat album are you thinking of? '
artist_prompt = "Who's the artist? "

# Let the user know how to quit.

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print('\nThanks for responding!')

