"""the game elements are devided here"""

building_a_house_list = [
    "Paster the walls",
    "Paint",
    "Lay the floor",
    "Tidy up",
    "Clean",
    "Look for a couch",
    "Look for chairs",
    "Find a TV",
    "Search for curtains",
    "Look for paintings",
    "clean up the garden",
    "Search for garden furniture",
    "Clean up the front yard",
    "Find a desk",
]


def convert_to_bin(number):
    return bin(number)

def clean_bin(bin_output):
    return bin_output[2:]

def turn_string_around(cleaned_bin):
    return cleaned_bin[::-1]

def make_list_of_string(turned_string_around):
    return list(turned_string_around)

def make_ints_in_elements_list(list_with_turned_strings):
    return list(map(int, list_with_turned_strings))

def show_gained_elements(list_with_elements, list_of_strings):
    return {k: v for k, v in zip(list_with_elements, list_of_strings)} 

def play_merge_game_with_lifes(elements, number_lifes):
    converter = convert_to_bin(number_lifes)
    cleaned_bin_string = clean_bin(converter)
    turned_string = turn_string_around(cleaned_bin_string)
    list_maker = make_list_of_string(turned_string)
    ints_maker = make_ints_in_elements_list(list_maker)
    outcome_gains = show_gained_elements(elements, ints_maker)
    return outcome_gains

