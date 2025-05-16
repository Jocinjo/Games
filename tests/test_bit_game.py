# import pytest
import sys
sys.path.append('.')
sys.path.append('./bit_game_2')
# import bit_game_2

dict_of_outcomes = {"convert_to_bin_outcome": '0b1000',
                    "clean_bin_outcome": '1000',
                    "turn_string_around_outcome": '0001',
                    "make_list_of_string_outcome": ['0', '0', '0', '1'],
                    "gained elements": "do not know yet"

                    }

def test_get_my_output():
    general_outcome = {'Paster the walls': 0, 'Paint': 0, 'Lay the floor': 0, 'Tidy up': 1}
    assert bit_game_2.get_my_output(8) == general_outcome

def test_convert_to_bin():
    assert bit_game_2.convert_to_bin(8) == dict_of_outcomes.get("convert_to_bin_outcome")

def test_clean_bin():
    assert bit_game_2.clean_bin('0b1000') == dict_of_outcomes.get("clean_bin_outcome")

def test_turn_string_around():
    assert bit_game_2.turn_string_around('1000') == dict_of_outcomes.get("turn_string_around_outcome")

def test_make_list_of_string():
    assert bit_game_2.make_list_of_string('0001') == dict_of_outcomes.get("make_list_of_string_outcome")


