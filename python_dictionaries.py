#6.1
person = {'first_name': 'michael', 'second_name': 'jones','age': '19', 'height': '5 foot 10', 'city': 'london', 'race': 'white'}
print(person['first_name'])
print(person['second_name'])
print(person['age'])
print(person['height'])
print(person['city'])
print(person['race'])

#6.2
favourite_number = {'michael': '10', 'jordan': '12', 'luke': '69'}
print(f"\nMichaels favourite number is {favourite_number['michael']}.")
print(f"\nJordan's favourite number is {favourite_number['jordan']}.")
print(f"\nLuke's favourite number is {favourite_number['luke']}.")

#6.3//6.4
python_key_words = {
    'variables': 'words which once defined represent value',
    'lists': 'stored values in order',
    'dictionaries': 'key value pairs saved together',
    'functions': 'defined values which represent chunks of code'
}

for key, value in python_key_words.items():
    print(f"{key}\n{value}\n")


#6.5
print(f"You need to repeat a series of code? Use {python_key_words['functions']}")

#6.6
favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'mike': ''
}

for name, language in favourite_language.items():
    if not language:  # empty string = no answer
        print(f"\n{name.title()}, you should answer the poll!")

 
#6.7
person_1 = {'first_name': 'michael', 'second_name': 'jones', 'age': '19'}
person_2 = {'first_name': 'jordan', 'second_name': 'zwart', 'age': '19'}
person_3 = {'first_name': 'luke', 'second_name': 'freitag', 'age': '20'}

people = [person_1, person_2, person_3]

for person in people:
    for key, value in person.items(): # key and value allow us to access key value pairs, .items() allow us to unpack each key value pair directly (in a loop)
        print(f"{key}: {value}") 
    print() # leaves a blank line between people

#6.8 // 6.9 - too simple
pet_1 = {'animal_kind': 'cat', 'owners_name': 'michael'}
pet_2 = {'animal_kind': 'dog', 'owners_name': 'jordan'}
pet_3 = {'animal_kind': 'hamster', 'owners_name': 'luke'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()

#6.10
fav_number_1 = {'name': 'michael', 'favourite_number': '10'}
fav_number_2 = {'name': 'jordan', 'favourite_number': ['12', '69']}

favourite_numbers = [fav_number_1, fav_number_2]

for number in favourite_numbers:
    for key, value in number.items():
        print(f"{key}: {value}")
    print()
