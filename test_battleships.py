import pytest
from battleships import *

# is_sunk tests

def test_is_sunk1():
    # Test asserts that cruiser is sunk
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True

def test_is_sunk2():
    # Test asserts that destroyer is sunk
    s = (0, 0, True, 2, {(0,0), (0,1)})
    assert is_sunk(s) == True

def test_is_sunk3():
    # Test asserts that submarine is sunk
    s = (9, 9, True, 1, {(9,9)})
    assert is_sunk(s) == True

def test_is_sunk4():
    # Test asserts that battleship is sunk
    s = (4, 4, False, 4, {(4,4), (5,4), (6,4), (7,4)})
    assert is_sunk(s) == True

def test_is_sunk5():
    # Test asserts that battleship is not sunk
    s = (4, 8, False, 4, {(4,8), (5,8), (6,8)})
    assert is_sunk(s) == False

def test_is_sunk6():
    # Test asserts that destroyer is not sunk
    s = (4, 1, False, 2, {(4,1)})
    assert is_sunk(s) == False

def test_is_sunk7():
    # Test asserts that cruiser is not sunk
    s = (2, 2, True, 3, {(2,2), (2,3)})
    assert is_sunk(s) == False

def test_is_sunk8():
    # Test asserts that submarine is not sunk
    s = (7, 6, False, 1, set())
    assert is_sunk(s) == False

# ship_type tests

def test_ship_type1():
    # Test asserts that ship_type is battleship
    ship = (0, 1, True, 4, set())
    assert ship_type(ship) == "battleship"

def test_ship_type2():
    # Test asserts that ship_type is cruiser
    ship = (2, 1, False, 3, set())
    assert ship_type(ship) == "cruiser"

def test_ship_type3():
    # Test asserts that ship_type is destroyer
    ship = (2, 6, True, 2, set())
    assert ship_type(ship) == "destroyer"

def test_ship_type4():
    # Test asserts that ship_type is submarine
    ship = (8, 8, True, 1, set())
    assert ship_type(ship) == "submarine"

def test_ship_type5():
    # Test asserts that ship_type (after hit) is destroyer
    ship = (6, 3, False, 2, {(6,3)})
    assert ship_type(ship) == "destroyer"

def test_ship_type6():
    # Test asserts that ship_type (after multiple hits) is battleship
    ship = (4, 3, True, 4, {(4,3), (4,4), (4,5)})
    assert ship_type(ship) == "battleship"

# is_open_sea tests

def test_is_open_sea1():
    # Test asserts that (4,5) (within squares occupied by ship4) is not open sea
    ship1 = (0, 1, True, 4, set())
    ship2 = (2, 1, False, 3, set())
    ship3 = (2, 6, True, 2, set())
    ship4 = (4, 4, True, 3, set())
    ship5 = (6, 3, False, 2, set())
    ship6 = (8, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6]
    assert is_open_sea(4, 5, fleet) == False

def test_is_open_sea2():
    # Test asserts that (5,3) is open sea
    ship1 = (0, 4, True, 1, set())
    ship2 = (1, 1, True, 2, set())
    ship3 = (1, 7, True, 2, set())
    ship4 = (3, 3, True, 1, set())
    ship5 = (3, 8, False, 4, set())
    ship6 = (4, 1, False, 2, set())
    ship7 = (4, 6, True, 1, set())
    ship8 = (7, 2, False, 3, set())
    ship9 = (7, 5, False, 3, set())
    ship10 = (9, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(5, 3, fleet) == True

def test_is_open_sea3():
    # Test asserts that (4,2) (diagonally adjacent to ship5) is not open sea
    ship1 = (0, 4, True, 1, set())
    ship2 = (0, 7, True, 2, set())
    ship3 = (1, 1, False, 2, set())
    ship4 = (2, 5, True, 4, set())
    ship5 = (3, 3, True, 1, set())
    ship6 = (4, 6, False, 3, set())
    ship7 = (4, 8, True, 1, set())
    ship8 = (5, 4, False, 2, set())
    ship9 = (7, 8, True, 1, set())
    ship10 = (8, 3, True, 3, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(4, 2, fleet) == False

def test_is_open_sea4():
    # Test asserts that (5,8) is open sea
    ship1 = (1, 0, True, 1, set())
    ship2 = (1, 2, True, 1, set())
    ship3 = (1, 7, True, 1, set())
    ship4 = (2, 4, True, 2, set())
    ship5 = (3, 0, False, 2, set())
    ship6 = (3, 2, False, 3, set())
    ship7 = (4, 4, True, 3, set())
    ship8 = (6, 0, False, 2, set())
    ship9 = (7, 3, True, 4, set())
    ship10 = (7, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(5, 8, fleet) == True

def test_is_open_sea5():
    # Test asserts that (7,5) (vertically adjacent to ship8) is not open sea
    ship1 = (0, 2, True, 1, set()) 
    ship2 = (1, 5, True, 2, set())
    ship3 = (2, 1, True, 3, set())
    ship4 = (3, 8, False, 3, set())
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 0, True, 4, set())
    ship7 = (7, 7, True, 1, set())
    ship8 = (8, 5, True, 1, set())
    ship9 = (9, 2, True, 2, set())
    ship10 = (9, 7, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(7, 5, fleet) == False

def test_is_open_sea6():
    # Test asserts that (1,6) (horizontally adjacent to ship2) is not open sea
    ship1 = (0, 7, True, 1, set())
    ship2 = (1, 5, True, 1, set())
    ship3 = (3, 1, True, 2, set())
    ship4 = (3, 5, False, 3, set())
    ship5 = (3, 8, True, 2, set())
    ship6 = (5, 8, False, 3, set())
    ship7 = (6, 0, True, 4, set())
    ship8 = (7, 6, False, 2, set())
    ship9 = (8, 4, True, 1, set())
    ship10 = (9, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(1, 6, fleet) == False

def test_is_open_sea7():
    # Test asserts that (4,3) (diagonally adjacent to ship3) is not open sea (additional test to test_is_open_sea3)
    ship1 = (0, 7, True, 1, set())
    ship2 = (1, 5, True, 1, set())
    ship3 = (3, 1, True, 2, set())
    ship4 = (3, 5, False, 3, set())
    ship5 = (3, 8, True, 2, set())
    ship6 = (5, 8, False, 3, set())
    ship7 = (6, 0, True, 4, set())
    ship8 = (7, 6, False, 2, set())
    ship9 = (8, 4, True, 1, set())
    ship10 = (9, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(4, 3, fleet) == False

def test_is_open_sea8():
    # Test asserts that (9,5) (diagonally adjacent to ship9) is not open sea (additional test to test_is_open_sea3 and test_is_open_sea7)
    ship1 = (0, 7, True, 1, set())
    ship2 = (1, 5, True, 1, set())
    ship3 = (3, 1, True, 2, set())
    ship4 = (3, 5, False, 3, set())
    ship5 = (3, 8, True, 2, set())
    ship6 = (5, 8, False, 3, set())
    ship7 = (6, 0, True, 4, set())
    ship8 = (7, 6, False, 2, set())
    ship9 = (8, 4, True, 1, set())
    ship10 = (9, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(9, 5, fleet) == False

def test_is_open_sea9():
    # Test asserts that (8,1) is open sea
    ship1 = (0, 7, True, 1, set())
    ship2 = (1, 5, True, 1, set())
    ship3 = (3, 1, True, 2, set())
    ship4 = (3, 5, False, 3, set())
    ship5 = (3, 8, True, 2, set())
    ship6 = (5, 8, False, 3, set())
    ship7 = (6, 0, True, 4, set())
    ship8 = (7, 6, False, 2, set())
    ship9 = (8, 4, True, 1, set())
    ship10 = (9, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(8, 1, fleet) == True

def test_is_open_sea10():
    # Test asserts that (7,1) (diagonally adjacent to ship7) is not opean sea (additional test to test_is_open_sea3, test_is_open_sea7 and test_is_open_sea8)
    ship1 = (0, 7, True, 1, set())
    ship2 = (1, 5, True, 1, set())
    ship3 = (3, 1, True, 2, set())
    ship4 = (3, 5, False, 3, set())
    ship5 = (3, 8, True, 2, set())
    ship6 = (5, 8, False, 3, set())
    ship7 = (6, 0, True, 4, set())
    ship8 = (7, 6, False, 2, set())
    ship9 = (8, 4, True, 1, set())
    ship10 = (9, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert is_open_sea(7, 1, fleet) == False

def test_is_open_sea11():
    # Test asserts that (4,5) is open sea with an empty fleet
    fleet = []
    assert is_open_sea(4, 5, fleet) == True

# ok_to_place_ship_at tests

def test_ok_to_place_ship_at1():
    # Test asserts that all the cells occupied by the ship (9, 1, True, 2, set()) are open sea
    ship1 = (0, 1, True, 4, set())
    ship2 = (2, 1, False, 3, set())
    ship3 = (2, 6, True, 2, set())
    ship4 = (4, 4, True, 3, set())
    ship5 = (6, 3, False, 2, set())
    ship6 = (8, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6]
    assert ok_to_place_ship_at(9, 1, True, 2, fleet) == True

def test_ok_to_place_ship_at2():
    #Test asserts that all the cells occupied by the ship (9, 8, True, 1, set()) are open sea
    ship1 = (0, 4, True, 1, set())
    ship2 = (1, 1, True, 2, set())
    ship3 = (1, 7, True, 2, set())
    ship4 = (3, 3, True, 1, set())
    ship5 = (3, 8, False, 4, set())
    ship6 = (4, 1, False, 2, set())
    ship7 = (4, 6, True, 1, set())
    ship8 = (7, 2, False, 3, set())
    ship9 = (7, 5, False, 3, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(9, 8, True, 1, fleet) == True

def test_ok_to_place_ship_at3():
    # Test asserts that all the cells occupied by the ships (8, 3, True, 3, set()) are open sea
    ship1 = (0, 4, True, 1, set())
    ship2 = (0, 7, True, 2, set())
    ship3 = (1, 1, False, 2, set())
    ship4 = (2, 5, True, 4, set())
    ship5 = (3, 3, True, 1, set())
    ship6 = (4, 6, False, 3, set())
    ship7 = (4, 8, True, 1, set())
    ship8 = (5, 4, False, 2, set())
    ship9 = (7, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(8, 3, True, 3, fleet) == True

def test_ok_to_place_ship_at4():
    # Test asserts that the ship (3, 1, False, 1, set()) (between cells occupied by ship5 and ship6) is not in open sea
    ship1 = (1, 0, True, 1, set())
    ship2 = (1, 2, True, 1, set())
    ship3 = (1, 7, True, 1, set())
    ship4 = (2, 4, True, 2, set())
    ship5 = (3, 0, False, 2, set())
    ship6 = (3, 2, False, 3, set())
    ship7 = (4, 4, True, 3, set())
    ship8 = (6, 0, False, 2, set())
    ship9 = (7, 3, True, 4, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(3, 1, False, 1, fleet) == False

def test_ok_to_place_ship_at5():
    # Test asserts that the ship (6, 0, True, 2, set()) (adjacent to cells occupied by ship5 and ship6) is not in open sea
    ship1 = (0, 2, True, 1, set()) 
    ship2 = (1, 5, True, 2, set())
    ship3 = (2, 1, True, 3, set())
    ship4 = (3, 8, False, 3, set())
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 0, True, 4, set())
    ship7 = (7, 7, True, 1, set())
    ship8 = (8, 5, True, 1, set())
    ship9 = (9, 2, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(6, 0, True, 2, fleet) == False

def test_ok_to_place_ship_at6():
    # Test asserts that the ship (9, 9, True, 2, set()) is not a legal placement because it goes out of bounds ((9,10) is not a cell on the board)
    ship1 = (0, 2, True, 1, set())
    ship2 = (1, 5, True, 2, set())
    ship3 = (2, 1, True, 3, set())
    ship4 = (3, 9, False, 3, set())
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 0, True, 4, set())
    ship7 = (7, 7, True, 1, set())
    ship8 = (8, 5, True, 1, set())
    ship9 = (9, 2, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(9, 9, True, 2, fleet) == False

def test_ok_to_place_ship_at7():
    # Test asserts that the ship (9, 9, False, 2, set()) is not a legal placement because it goes out of bounds ((10,9) is not a cell on the board)
    ship1 = (0, 2, True, 1, set())
    ship2 = (1, 5, True, 2, set())
    ship3 = (2, 1, True, 3, set())
    ship4 = (3, 9, False, 3, set())
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 0, True, 4, set())
    ship7 = (7, 7, True, 1, set())
    ship8 = (8, 5, True, 1, set())
    ship9 = (9, 2, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(9, 9, False, 2, fleet) == False

def test_ok_to_place_ship_at8():
    # Test asserts that the ship (9, 2, False, 2, set()) is not a legal placement because it goes out of bounds ((10,2) is not a cell on the board)
    ship1 = (0, 2, True, 1, set())
    ship2 = (1, 5, True, 2, set())
    ship3 = (2, 1, True, 3, set())
    ship4 = (3, 9, False, 3, set())
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 0, True, 4, set())
    ship7 = (7, 7, True, 1, set())
    ship8 = (8, 5, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8]
    assert ok_to_place_ship_at(9, 2, False, 2, fleet) == False

def test_ok_to_place_ship_at9():
    # Test asserts that the ship (9, 10, True, 1, set()) is not a legal placement because the ship is situated out of bounds
    ship1 = (0, 2, True, 1, set())
    ship2 = (1, 5, True, 2, set())
    ship3 = (2, 1, True, 3, set())
    ship4 = (3, 9, False, 3, set())
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 0, True, 4, set())
    ship7 = (7, 7, True, 1, set())
    ship8 = (8, 5, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8]
    assert ok_to_place_ship_at(9, 10, True, 1, fleet) == False

def test_ok_to_place_ship_at10():
    # Test asserts that the cell occupied by ship (8, 6, True, 1, set()) is in open sea
    ship1 = (0, 0, False, 4, set())
    ship2 = (0, 2, False, 3, set())
    ship3 = (0, 4, False, 3, set())
    ship4 = (0, 6, False, 2, set())
    ship5 = (5, 0, False, 2, set())
    ship6 = (5, 2, False, 2, set())
    ship7 = (8, 0, True, 1, set())
    ship8 = (8, 2, True, 1, set())
    ship9 = (8, 4, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(8, 6, True, 1, fleet) == True

def test_ok_to_place_ship_at11():
    # Test asserts that the cell occupied by ship (8, 5, True, 1, set()) (where (8,5) is horizontally adjacent to ship9) is not in open sea
    ship1 = (0, 0, False, 4, set())
    ship2 = (0, 2, False, 3, set())
    ship3 = (0, 4, False, 3, set())
    ship4 = (0, 6, False, 2, set())
    ship5 = (5, 0, False, 2, set())
    ship6 = (5, 2, False, 2, set())
    ship7 = (8, 0, True, 1, set())
    ship8 = (8, 2, True, 1, set())
    ship9 = (8, 4, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert ok_to_place_ship_at(8, 5, True, 1, fleet) == False

# place_ship_at tests

def test_place_ship_at1():
    # Test asserts that ship (9, 1, True, 2, set()) is added correctly to fleet
    ship1 = (0, 1, True, 4, set())
    ship2 = (2, 1, False, 3, set())
    ship3 = (2, 6, True, 2, set())
    ship4 = (4, 4, True, 3, set())
    ship5 = (6, 3, False, 2, set())
    ship6 = (8, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6]
    assert place_ship_at(9, 1, True, 2, fleet) == [(0, 1, True, 4, set()),
    (2, 1, False, 3, set()),
    (2, 6, True, 2, set()),
    (4, 4, True, 3, set()),
    (6, 3, False, 2, set()),
    (8, 8, True, 1, set()),
    (9, 1, True, 2, set())]

def test_place_ship_at2():
    # Test asserts that ship (9, 8, True, 1, set()) is added correctly to fleet
    ship1 = (0, 4, True, 1, set())
    ship2 = (1, 1, True, 2, set())
    ship3 = (1, 7, True, 2, set())
    ship4 = (3, 3, True, 1, set())
    ship5 = (3, 8, False, 4, set())
    ship6 = (4, 1, False, 2, set())
    ship7 = (4, 6, True, 1, set())
    ship8 = (7, 2, False, 3, set())
    ship9 = (7, 5, False, 3, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert place_ship_at(9, 8, True, 1, fleet) == [(0, 4, True, 1, set()),
    (1, 1, True, 2, set()),
    (1, 7, True, 2, set()),
    (3, 3, True, 1, set()),
    (3, 8, False, 4, set()),
    (4, 1, False, 2, set()),
    (4, 6, True, 1, set()),
    (7, 2, False, 3, set()),
    (7, 5, False, 3, set()),
    (9, 8, True, 1, set())]

def test_place_ship_at3():
    # Test asserts that ship (8, 3, True, 3, set()) is added correctly to fleet
    ship1 = (0, 4, True, 1, set())
    ship2 = (0, 7, True, 2, set())
    ship3 = (1, 1, False, 2, set())
    ship4 = (2, 5, True, 4, set())
    ship5 = (3, 3, True, 1, set())
    ship6 = (4, 6, False, 3, set())
    ship7 = (4, 8, True, 1, set())
    ship8 = (5, 4, False, 2, set())
    ship9 = (7, 8, True, 1, set())
    ship10 = (8, 3, True, 3, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert place_ship_at(8, 3, True, 3, fleet) == [(0, 4, True, 1, set()),
    (0, 7, True, 2, set()),
    (1, 1, False, 2, set()),
    (2, 5, True, 4, set()),
    (3, 3, True, 1, set()),
    (4, 6, False, 3, set()),
    (4, 8, True, 1, set()),
    (5, 4, False, 2, set()),
    (7, 8, True, 1, set()),
    (8, 3, True, 3, set())]

def test_place_ship_at4():
    # Test asserts that ship (7, 3, True, 4, fleet) is added correctly to fleet
    ship1 = (1, 0, True, 1, set())
    ship2 = (1, 2, True, 1, set())
    ship3 = (1, 7, True, 1, set())
    ship4 = (2, 4, True, 2, set())
    ship5 = (3, 0, False, 2, set())
    ship6 = (3, 2, False, 3, set())
    ship7 = (4, 4, True, 3, set())
    ship8 = (6, 0, False, 2, set())
    ship9 = (7, 3, True, 4, set())
    ship9 = (7, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert place_ship_at(7, 3, True, 4, fleet) == [(1, 0, True, 1, set()),
    (1, 2, True, 1, set()),
    (1, 7, True, 1, set()),
    (2, 4, True, 2, set()),
    (3, 0, False, 2, set()),
    (3, 2, False, 3, set()),
    (4, 4, True, 3, set()),
    (6, 0, False, 2, set()),
    (7, 8, True, 1, set()),
    (7, 3, True, 4, set())]

def test_place_ship_at5():
    # Test asserts that actual fleet and expected fleet are identical after place_ship_at and sort method are used
    ship1 = (0, 2, True, 1, set()) 
    ship2 = (1, 5, True, 2, set())
    ship3 = (2, 1, True, 3, set())
    ship4 = (3, 8, False, 3, set())
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 7, True, 1, set())
    ship7 = (8, 5, True, 1, set())
    ship8 = (9, 2, True, 2, set())
    ship9 = (9, 7, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    actual = place_ship_at(7, 0, True, 4, fleet)
    actual.sort()
    expected = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, (7, 0, True, 4, set())]
    expected.sort()
    assert actual == expected

# check_if_hits tests

def test_check_if_hits1():
    # Test asserts that a hit in (6,3) will result in a hit on ship5
    ship1 = (0, 1, True, 4, set())
    ship2 = (2, 1, False, 3, set())
    ship3 = (2, 6, True, 2, set())
    ship4 = (4, 4, True, 3, set())
    ship5 = (6, 3, False, 2, set())
    ship6 = (8, 8, True, 1, set())
    ship7 = (9, 1, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7]
    assert check_if_hits(6, 3, fleet) == True

def test_check_if_hits2():
    # Test asserts that a hit in (8,2) will result in a hit on ship8
    ship1 = (0, 4, True, 1, set())
    ship2 = (1, 1, True, 2, set())
    ship3 = (1, 7, True, 2, set())
    ship4 = (3, 3, True, 1, set())
    ship5 = (3, 8, False, 4, set())
    ship6 = (4, 1, False, 2, set())
    ship7 = (4, 6, True, 1, set())
    ship8 = (7, 2, False, 3, set())
    ship9 = (7, 5, False, 3, set())
    ship10 = (9, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert check_if_hits(8, 2, fleet) == True

def test_check_if_hits3():
    # Test asserts that a hit in (8,8) (vertically adjacent to the cell occupied by ship9) will not hit any cell of the ships in fleet
    ship1 = (0, 4, True, 1, set())
    ship2 = (0, 7, True, 2, set())
    ship3 = (1, 1, False, 2, set())
    ship4 = (2, 5, True, 4, set())
    ship5 = (3, 3, True, 1, set())
    ship6 = (4, 6, False, 3, set())
    ship7 = (4, 8, True, 1, set())
    ship8 = (5, 4, False, 2, set())
    ship9 = (7, 8, True, 1, set())
    ship10 = (8, 3, True, 3, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert check_if_hits(8, 8, fleet) == False

def test_check_if_hits4():
    # Test asserts that a hit in (5,2) will result in a hit on ship6
    ship1 = (1, 0, True, 1, set())
    ship2 = (1, 2, True, 1, set())
    ship3 = (1, 7, True, 1, set())
    ship4 = (2, 4, True, 2, set())
    ship5 = (3, 0, False, 2, set())
    ship6 = (3, 2, False, 3, set())
    ship7 = (4, 4, True, 3, set())
    ship8 = (6, 0, False, 2, set())
    ship9 = (7, 3, True, 4, set())
    ship10 = (7, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert check_if_hits(5, 2, fleet) == True

def test_check_if_hits5():
    # Test asserts that a hit in (4,2) (diagonally adjacent to the cell occupied by ship5) will not hit any cell of the ships in fleet
    ship1 = (0, 2, True, 1, set()) 
    ship2 = (1, 5, True, 2, set())
    ship3 = (2, 1, True, 3, set())
    ship4 = (3, 8, False, 3, set())
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 0, True, 4, set())
    ship7 = (7, 7, True, 1, set())
    ship8 = (8, 5, True, 1, set())
    ship9 = (9, 2, True, 2, set())
    ship10 = (9, 7, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert check_if_hits(4, 2, fleet) == False

# hit tests

def test_hit1():
    # Test asserts that a hit in (6,3) will result in a hit on ship5, and that the fleet and ship will be updated correctly to reflect the tuple
    ship1 = (0, 1, True, 4, set())
    ship2 = (2, 1, False, 3, set())
    ship3 = (2, 6, True, 2, set())
    ship4 = (4, 4, True, 3, set())
    ship5 = (6, 3, False, 2, set())
    ship6 = (8, 8, True, 1, set())
    ship7 = (9, 1, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7]
    assert hit(6, 3, fleet) == ([(0, 1, True, 4, set()),
    (2, 1, False, 3, set()),
    (2, 6, True, 2, set()),
    (4, 4, True, 3, set()),
    (6, 3, False, 2, {(6,3)}),
    (8, 8, True, 1, set()),
    (9, 1, True, 2, set())], (6, 3, False, 2, {(6,3)}))

def test_hit2():
    # Test asserts that a hit in (8,2) will result in a hit on ship8, and that the fleet and ship will be updated correctly to reflect the tuple
    ship1 = (0, 4, True, 1, set())
    ship2 = (1, 1, True, 2, {(1,1)})
    ship3 = (1, 7, True, 2, set())
    ship4 = (3, 3, True, 1, set())
    ship5 = (3, 8, False, 4, {(3,8), (4,8)})
    ship6 = (4, 1, False, 2, set())
    ship7 = (4, 6, True, 1, set())
    ship8 = (7, 2, False, 3, set())
    ship9 = (7, 5, False, 3, set())
    ship10 = (9, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert hit(8, 2, fleet) == ([(0, 4, True, 1, set()),
    (1, 1, True, 2, {(1,1)}),
    (1, 7, True, 2, set()), 
    (3, 3, True, 1, set()),
    (3, 8, False, 4, {(3,8), (4,8)}),
    (4, 1, False, 2, set()),
    (4, 6, True, 1, set()),
    (7, 2, False, 3, {(8,2)}),
    (7, 5, False, 3, set()),
    (9, 8, True, 1, set())], (7, 2, False, 3, {(8,2)}))
    
def test_hit3():
    # Test asserts that a hit in (8,5) will result in a hit on ship10, and that the fleet and ship will be updated correctly to reflect the tuple
    ship1 = (0, 4, True, 1, set())
    ship2 = (0, 7, True, 2, set())
    ship3 = (1, 1, False, 2, set())
    ship4 = (2, 5, True, 4, set())
    ship5 = (3, 3, True, 1, set())
    ship6 = (4, 6, False, 3, {(4,6), (5,6)})
    ship7 = (4, 8, True, 1, set())
    ship8 = (5, 4, False, 2, {(6,4)})
    ship9 = (7, 8, True, 1, set())
    ship10 = (8, 3, True, 3, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert hit(8, 5, fleet) == ([(0, 4, True, 1, set()),
    (0, 7, True, 2, set()),
    (1, 1, False, 2, set()),
    (2, 5, True, 4, set()),
    (3, 3, True, 1, set()),
    (4, 6, False, 3, {(4,6), (5,6)}),
    (4, 8, True, 1, set()),
    (5, 4, False, 2, {(6,4)}),
    (7, 8, True, 1, set()),
    (8, 3, True, 3, {(8,5)})], (8, 3, True, 3, {(8,5)}))
    
def test_hit4():
    # Test asserts that a hit in (4,5) will result in a hit on ship7, and that the fleet and ship will be updated correctly to reflect the tuple
    ship1 = (1, 0, True, 1, set())
    ship2 = (1, 2, True, 1, set())
    ship3 = (1, 7, True, 1, set())
    ship4 = (2, 4, True, 2, {(2, 5)})
    ship5 = (3, 0, False, 2, {(4,0)})
    ship6 = (3, 2, False, 3, {(3,2), (4,2)})
    ship7 = (4, 4, True, 3, set())
    ship8 = (6, 0, False, 2, set())
    ship9 = (7, 3, True, 4, {(7,3), (7,4), (7,5)})
    ship10 = (7, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert hit(4, 5, fleet) == ([(1, 0, True, 1, set()),
    (1, 2, True, 1, set()),
    (1, 7, True, 1, set()),
    (2, 4, True, 2, {(2, 5)}),
    (3, 0, False, 2, {(4,0)}),
    (3, 2, False, 3, {(3,2), (4,2)}),
    (4, 4, True, 3, {(4,5)}),
    (6, 0, False, 2, set()),
    (7, 3, True, 4, {(7,3), (7,4), (7,5)}),
    (7, 8, True, 1, set())],  (4, 4, True, 3, {(4,5)}))

def test_hit5():
    # Test asserts that a hit in (9,8) will result in a hit on ship10, and that the fleet and ship will be updated correctly to reflect the tuple
    ship1 = (0, 2, True, 1, set()) 
    ship2 = (1, 5, True, 2, {(1,5)})
    ship3 = (2, 1, True, 3, {(2,3)})
    ship4 = (3, 8, False, 3, {(5,8)})
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 0, True, 4, {(7,2), (7,3)})
    ship7 = (7, 7, True, 1, set())
    ship8 = (8, 5, True, 1, set())
    ship9 = (9, 2, True, 2, {(9,3)})
    ship10 = (9, 7, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert hit(9, 8, fleet) == ([(0, 2, True, 1, set()),
    (1, 5, True, 2, {(1,5)}),
    (2, 1, True, 3, {(2,3)}),
    (3, 8, False, 3, {(5,8)}),
    (5, 1, True, 1, set()),
    (7, 0, True, 4, {(7,2), (7,3)}),
    (7, 7, True, 1, set()),
    (8, 5, True, 1, set()),
    (9, 2, True, 2, {(9,3)}),
    (9, 7, True, 2, {(9,8)})], (9, 7, True, 2, {(9,8)}))

def test_hit6():
    # Test asserts that a hit in (7,7) will result in a hit on ship7, sinking the ship, and that the fleet and ship will be updated correctly to reflect the tuple
    ship1 = (0, 2, True, 1, set())
    ship2 = (1, 5, True, 2, set())
    ship3 = (2, 1, True, 3, set())
    ship4 = (3, 9, False, 3, set())
    ship5 = (5, 1, True, 1, set())
    ship6 = (7, 0, True, 4, set())
    ship7 = (7, 7, True, 1, set())
    ship8 = (8, 5, True, 1, set())
    ship9 = (9, 2, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9]
    assert hit(7, 7, fleet) == ([(0, 2, True, 1, set()),
    (1, 5, True, 2, set()),
    (2, 1, True, 3, set()),
    (3, 9, False, 3, set()),
    (5, 1, True, 1, set()),
    (7, 0, True, 4, set()),
    (8, 5, True, 1, set()),
    (9, 2, True, 2, set())], (7, 7, True, 1, {(7,7)}))

def test_hit7():
    # Test asserts that a hit in (2,8) will result in a hit on ship3, sinking the ship, and that the fleet and ship will be updated correctly to reflect the tuple
    ship1 = (2, 1, False, 3, set())
    ship2 = (2, 3, True, 1, set())
    ship3 = (2, 5, True, 4, {(2,5), (2,6), (2,7)})
    ship4 = (4, 8, True, 2, set())
    ship5 = (5, 5, False, 3, set())
    ship6 = (6, 9, True, 1, set())
    ship7 = (7, 0, True, 1, set())
    ship8 = (9, 0, True, 2, set())
    ship9 = (9, 5, True, 1, set())
    ship10 = (9, 8, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert hit(2, 8, fleet) == ([(2, 1, False, 3, set()),
    (2, 3, True, 1, set()),
    (4, 8, True, 2, set()),
    (5, 5, False, 3, set()),
    (6, 9, True, 1, set()),
    (7, 0, True, 1, set()),
    (9, 0, True, 2, set()),
    (9, 5, True, 1, set()),
    (9, 8, True, 2, set())], (2, 5, True, 4, {(2,5), (2,6), (2,7), (2,8)}))

def test_hit8():
    # Test asserts that a hit in (8,6) will result in a hit on ship10, sinking the ship, and that the fleet and ship will be updated correctly to reflect the tuple
    ship1 = (0, 0, False, 4, {(0,0), (2,0)})
    ship2 = (0, 2, False, 3, {(0,2), (2,2)})
    ship3 = (0, 4, False, 3, {(0,4), (2,4)})
    ship4 = (0, 6, False, 2, {(1,6)})
    ship5 = (5, 0, False, 2, {(6,0)})
    ship6 = (5, 2, False, 2, {(5,2)})
    ship7 = (8, 0, True, 1, set())
    ship8 = (8, 2, True, 1, set())
    ship9 = (8, 4, True, 1, set())
    ship10 = (8, 6, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert hit(8, 6, fleet) == ([(0, 0, False, 4, {(0,0), (2,0)}),
    (0, 2, False, 3, {(0,2), (2,2)}),
    (0, 4, False, 3, {(0,4), (2,4)}),
    (0, 6, False, 2, {(1,6)}),
    (5, 0, False, 2, {(6,0)}),
    (5, 2, False, 2, {(5,2)}),
    (8, 0, True, 1, set()),
    (8, 2, True, 1, set()),
    (8, 4, True, 1, set())], (8, 6, True, 1, {(8,6)}))

def test_hit9():
    # Test asserts that a hit in (8,6) will result in a hit on ship10, sinking the ship
    # And that the hit function will not return a tuple with the sunk ship still in the fleet
    ship1 = (0, 0, False, 4, {(0,0), (2,0)})
    ship2 = (0, 2, False, 3, {(0,2), (2,2)})
    ship3 = (0, 4, False, 3, {(0,4), (2,4)})
    ship4 = (0, 6, False, 2, {(1,6)})
    ship5 = (5, 0, False, 2, {(6,0)})
    ship6 = (5, 2, False, 2, {(5,2)})
    ship7 = (8, 0, True, 1, set())
    ship8 = (8, 2, True, 1, set())
    ship9 = (8, 4, True, 1, set())
    ship10 = (8, 6, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert hit(8, 6, fleet) != ([(0, 0, False, 4, {(0,0), (2,0)}),
    (0, 2, False, 3, {(0,2), (2,2)}),
    (0, 4, False, 3, {(0,4), (2,4)}),
    (0, 6, False, 2, {(1,6)}),
    (5, 0, False, 2, {(6,0)}),
    (5, 2, False, 2, {(5,2)}),
    (8, 0, True, 1, set()),
    (8, 2, True, 1, set()),
    (8, 4, True, 1, set()),
    (8, 6, True, 1, {(8,6)})], (8, 6, True, 1, {(8,6)}))

def test_hit10():
    # Test asserts that a hit in (1,2) will result in a hit on ship2, sinking the ship, and that the fleet and ship will be updated correctly to reflect the tuple
    ship1 = (0, 0, False, 4, {(0,0), (2,0)})
    ship2 = (0, 2, False, 3, {(0,2), (2,2)})
    ship3 = (0, 4, False, 3, {(0,4), (2,4)})
    ship4 = (0, 6, False, 2, {(1,6)})
    ship5 = (5, 0, False, 2, {(6,0)})
    ship6 = (5, 2, False, 2, {(5,2)})
    ship7 = (8, 0, True, 1, set())
    ship8 = (8, 2, True, 1, set())
    ship9 = (8, 4, True, 1, set())
    ship10 = (8, 6, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert hit(1, 2, fleet) == ([(0, 0, False, 4, {(0,0), (2,0)}),
    (0, 4, False, 3, {(0,4), (2,4)}),
    (0, 6, False, 2, {(1,6)}),
    (5, 0, False, 2, {(6,0)}),
    (5, 2, False, 2, {(5,2)}),
    (8, 0, True, 1, set()),
    (8, 2, True, 1, set()),
    (8, 4, True, 1, set()),
    (8, 6, True, 1, set())], (0, 2, False, 3, {(0,2), (1,2), (2,2)}))   

# are_unsunk_ships_left tests   

def test_are_unsunk_ships_left1():
    # As seven ships are still unsunk, test asserts that unsunk_ships_left(fleet) is True
    ship1 = (0, 1, True, 4, set())
    ship2 = (2, 1, False, 3, set())
    ship3 = (2, 6, True, 2, set())
    ship4 = (4, 4, True, 3, set())
    ship5 = (6, 3, False, 2, set())
    ship6 = (8, 8, True, 1, set())
    ship7 = (9, 1, True, 2, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7]
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left2():
    # As 10 ships are still unsunk, test asserts that unsunk_ships_left(fleet) is True
    ship1 = (0, 4, True, 1, set())
    ship2 = (1, 1, True, 2, set())
    ship3 = (1, 7, True, 2, set())
    ship4 = (3, 3, True, 1, set())
    ship5 = (3, 8, False, 4, set())
    ship6 = (4, 1, False, 2, set())
    ship7 = (4, 6, True, 1, set())
    ship8 = (7, 2, False, 3, set())
    ship9 = (7, 5, False, 3, set())
    ship10 = (9, 8, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10]
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left3():
    # As 0 ships are still unsunk, test asserts that unsunk_ships_left(fleet) is False
    fleet = []
    assert are_unsunk_ships_left(fleet) == False

def test_are_unsunk_ships_left4():
    # As 5 ships are still unsunk, the test asserts that unsunk_ships_left(fleet) is True
    ship1 = (0, 4, True, 1, set())
    ship2 = (0, 7, True, 2, set())
    ship3 = (1, 1, False, 2, set())
    ship4 = (2, 5, True, 4, set())
    ship5 = (3, 3, True, 1, set())
    fleet = [ship1, ship2, ship3, ship4, ship5]
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left5():
    # As 3 ships are still unsunk, the test asserts that unsunk_ships_left(fleet) is True
    ship1 = (1, 0, True, 1, set())
    ship2 = (1, 2, True, 1, set())
    ship3 = (1, 7, True, 1, set())
    fleet = [ship1, ship2, ship3]
    assert are_unsunk_ships_left(fleet) == True
