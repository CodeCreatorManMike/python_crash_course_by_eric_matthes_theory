#8.1
def display_message():
    print('\nI am currently learning python at the moment')

display_message()

#8.2
def favourite_book(title):
    print(f"\nOne of my favourite books is {title.title()}.")

favourite_book('oxygen thief')

#8.3 // 8.4
def make_shirt(size='large', text='I LOVE PYTHON'):
    print(f"\nI'd like a size {size} shirt, that says {text} on it.")

make_shirt('medium', 'CRAZY') # positional arguments
make_shirt(size='medium', text='CRAZY') # keyword arguments

make_shirt()

#8.5
def describe_city(city_name = 'durban', country_name = 'south africa'):
    print(f"\n{city_name.title()} is in {country_name.title()}")

describe_city()

describe_city(city_name='cape town')
describe_city(country_name='southern africa')


#8.6
def city_country(city_name, country_name):
    city_country_name = f"{city_name}, {country_name}"
    return city_country_name.title()


home_town = city_country('\ndurban', 'south africa')
dream_town = city_country('\nnew york', 'united states of america')
current_town = city_country('\nlondon', 'united kingdom')
print(home_town)
print(dream_town)
print(current_town)


#8.7 // 8.8
def build_album(artist_name, album_name, number_of_songs=None):
    album = {"Artist": artist_name, "Album Name": album_name}
    if number_of_songs is not None:
        album["Number Of Songs"] = number_of_songs
    return album

# ---- Album input loop ----
while True:
    print('\nPlease tell me your favourite album!')
    print('Enter "q" at any time to quit')

    artist_name = input("\nArtist Name: ").strip()
    if artist_name.lower() == 'q':
        break
    if artist_name == "":
        print("Artist name can't be empty. Try again.")
        continue

    album_name = input("Album Name: ").strip()
    if album_name.lower() == 'q':
        break
    if album_name == "":
        print("Album name can't be empty. Try again.")
        continue

    raw_num = input("Number Of Songs (press Enter to skip): ").strip()
    if raw_num.lower() == 'q':
        break
    if raw_num == "":
        number_of_songs = None
    else:
        try:
            number_of_songs = int(raw_num)
        except ValueError:
            print("Please enter a whole number, or press Enter to skip.")
            continue  # restart the loop without exiting

    album = build_album(artist_name, album_name, number_of_songs)
    print(f"\nYour album dictionary: {album}")

# 8.9 // 8.10 // 8.11
un_printed_messages = [
    'I love Python',
    'I want to learn C++ next',
    "I'm hoping to become an AI engineer",
]

printed_messages = []

def show_messages(messages, printed_list):
    #Print each message and move it from messages to printed_list.
    while messages:
        current_message = messages.pop()
        print(current_message)
        printed_list.append(current_message)
    return printed_list

# Pass a copy of the list to preserve the original
un_printed_messages_copy = un_printed_messages[:]
show_messages(un_printed_messages_copy, printed_messages)

print("\nOriginal un_printed_messages:", un_printed_messages)
print("\nCopied un_printed_messages (now emptied):", un_printed_messages_copy)
print("\nPrinted messages:", printed_messages)

# 8.12
sandwhich_toppings = []

def make_sandwhich(*sandwhich_toppings):
    print(sandwhich_toppings)

make_sandwhich('ham', 'salami', 'pepperoni', 'mayo', 'lettuce')
make_sandwhich('cheese', 'ham')

# 8.13 - in modules file python_module_build_profile

# 8.14
def build_cars(manufacturer, model_name, **kwargs):
    kwargs['car_manufacturer'] = manufacturer
    kwargs['car_model_name'] = model_name
    return kwargs

car = build_cars('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 8.15
import python_module_build_profile 

my_user_profile = python_module_build_profile.build_profile('michael', 'jones',
                                location='london',
                                field='computer science/AI',
                                current_learning='python',
                                passion='music')

print(my_user_profile)

# 8.16 - 8.17
import python_module_build_profile 
from python_module_build_profile import build_profile
from python_module_build_profile import build_profile as x
import python_module_build_profile as bp
from python_module_build_profile import *

# End of chapter
