# import pytest
import sys
sys.path.append('.')
sys.path.append('./bit_game_2')
# import bit_game_2

def test_get_my_output():
    outcome = {'Paster the walls': 0, 'Paint': 0, 'Lay the floor': 0, 'Tidy up': 1}
    assert bit_game_2.get_my_output(8) == outcome