# import pandas as pd
# import matplotlib.pyplot as plt

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
# print(building_a_house_list)

def get_my_output(levens):
    bin_string = bin(levens)
    clean_string = bin_string[2:]
    turned_string = clean_string[::-1]
    list_of_elements_binary_string = list(turned_string)
    list_of_elements_binary_int = list(map(int, list_of_elements_binary_string))
    gespaarde_elementen = {
        k: v for k, v in zip(building_a_house_list, list_of_elements_binary_int)
    }

    return gespaarde_elementen

print(get_my_output(8))

def convert_to_bin(number):
    # print(bin(number))
    return bin(number)

def clean_bin(bin_output):
    return bin_output[2:]

def turn_string_around(cleaned_bin):
    return cleaned_bin[::-1]

def make_list_of_string(turned_string_around):
    return list(turned_string_around)

def show_gained_elements(list_with_elements, list_of_strings):
    return {k: v for k, v in zip(list_with_elements, list_of_strings)} 

