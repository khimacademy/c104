'''
6-8. 애완동물
딕셔너리를 여러 개 만들고 이름은 애완동물 이름으로 하세요. 각 딕셔너리에 동물 종류와 주인 이름을 쓰세요. 이들 딕셔너리를 pets 리스트에 저장하세요. 리스트에 루프를 실행하고 각 애완동물에 대해 알고 있는 것을 모두 출력하세요.

Output:

Here's what I know about john:
    weight: 43
    animal type: python
    name: john
    owner: guido
    eats: bugs

Here's what I know about clarence:
    weight: 2
    animal type: chicken
    name: clarence
    owner: tiffany
    eats: seeds

Here's what I know about peso:
    weight: 37
    animal type: dog
    name: peso
    owner: eric
    eats: shoes
'''

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'] + ':')
    for key, value in pet.items():
        print('\t' + key + ': ' + str(value))

