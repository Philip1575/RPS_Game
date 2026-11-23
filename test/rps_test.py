
# this is the "test/rps_test.py" file...

from app.rps import determine_winner, generate_random_choice, VALID_OPTIONS


def test_example():
    assert 2 + 2 == 4


def test_random_choice():
    # the computer's choice should always be one of the valid options
    for _ in range(20):
        assert generate_random_choice() in VALID_OPTIONS


def test_winners():
    # tests for all edge cases:

    assert determine_winner(u="rock", c="rock") == "TIE GAME"
    assert determine_winner(u="rock", c="paper") == "COMPUTER WINS"
    assert determine_winner(u="rock", c="scissors") == "USER WINS"

    assert determine_winner(u="paper", c="rock") == "USER WINS"
    assert determine_winner(u="paper", c="paper") == "TIE GAME"
    assert determine_winner(u="paper", c="scissors") == "COMPUTER WINS"

    assert determine_winner(u="scissors", c="scissors") == "TIE GAME"
    assert determine_winner(u="scissors", c="paper") == "USER WINS"
    assert determine_winner(u="scissors", c="rock") == "COMPUTER WINS"



    # you may have more test functions here, but this is a good start for now
    
    # another test function here