#see the readme.md file for description and data 

import random

def is_sunk(ship):
    '''Returns Boolean value, which is True if ship is sunk and False otherwise.'''
    # If number of hits matches number of squares occupied by the ship, return True, else False
    if len(ship[4]) == ship[3]:
        return True
    else:
        return False
    
def ship_type(ship):
    '''Returns one of the strings "battleship", "cruiser", "destroyer", or "submarine" identifying the type of ship.'''
    # The length of the item at the 3rd index in the ship tuple indicates which type o ship it is
    if ship[3] == 1:
        return "submarine"
    elif ship[3] == 2:
        return "destroyer"
    elif ship[3] == 3:
        return "cruiser"
    elif ship[3] == 4:
        return "battleship"

def is_open_sea(row, column, fleet):
    '''Checks if the square given by row and column neither contains nor is adjacent
    (horizontally, vertically, or diagonally) to some ship in fleet. Returns Boolean True
    if so and False otherwise.'''
    # Determine what the occupied cells are
    # Append occupied cells to a list
    occupied_cells = []
    target_cell = tuple((row, column))
    open_sea = True
    for s in range(len(fleet)):
        occupied_cells.append(tuple((fleet[s][0], fleet[s][1])))
        if fleet[s][2] == True:
            for i in range(1, fleet[s][3]):
                cell = tuple((fleet[s][0], fleet[s][1]+i))
                occupied_cells.append(cell)

        elif fleet[s][2] == False:
            for i in range(1, fleet[s][3]):
                cell = tuple((fleet[s][0]+i, fleet[s][1]))
                occupied_cells.append(cell)

    # Once list of occupied cells are generated, ensure target cell is not within 2 cell circumference of any occupied cell
    for i in range(len(occupied_cells)):
        if abs(target_cell[0]-occupied_cells[i][0]) < 2:
            if abs(target_cell[1]-occupied_cells[i][1]) < 2:
                open_sea = False
            else:
                pass
        elif abs(target_cell[1]-occupied_cells[i][1]) < 2:
            if abs(target_cell[0]-occupied_cells[i][0]) < 2:
                open_sea = False
            else:
                pass

    return open_sea

            
def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    '''Checks if addition of a ship, specified by row, column, horizontal, and length as in ship representation above,
    to the fleet results in a legal arrangement (see the figure above).
    If so, the function returns Boolean True and it returns False otherwise.
    This function makes use of the function is_open_sea.'''
    # Generate list of cells occupied by proposed new ship
    new_ship = tuple((row, column, horizontal, length, set()))
    ship_cells = []
    ok_to_place_ship_at = True
    ship_cells.append(tuple((new_ship[0], new_ship[1])))
    if new_ship[2] == True:
        for i in range(1, new_ship[3]):
            cell = tuple((new_ship[0], new_ship[1]+i))
            ship_cells.append(cell)
    elif new_ship[2] == False:
        for i in range(1, new_ship[3]):
            cell = tuple((new_ship[0]+i, new_ship[1]))
            ship_cells.append(cell)

    # If each cell returns true for is_open_sea, and row and column numbers do not exceed 9, return True, else False
    for c in ship_cells:
        if is_open_sea(c[0], c[1], fleet) == True:
            if c[0] <= 9 and c[1] <= 9:
                pass
            else:
                ok_to_place_ship_at = False
        else:
            ok_to_place_ship_at = False
            
    return ok_to_place_ship_at    

def place_ship_at(row, column, horizontal, length, fleet):
    '''Returns a new fleet that is the result of adding a ship, specified by row, column, horizontal, and length
    as in ship representation above, to fleet. It may be assumed that the resulting arrangement of the new fleet is legal.'''
    # Create a tuple for new_ship from the function's arguments
    # Append the new_ship tuple to the list fleet and return this new fleet
    new_ship = tuple((row, column, horizontal, length, set()))
    fleet.append(new_ship)
    return fleet

def randomly_place_all_ships():
    '''Returns a fleet that is a result of a random legal arrangement of the 10 ships in the ocean.
    This function makes use of the functions ok_to_place_ship_at and place_ship_at.'''
    # Begin with an empty list for fleet
    fleet = []
    battleships = False
    cruisers = False
    destroyers = False
    submarines = False

    # Start with the largest ship (battleship) and progress to the smallest ships (submarine)
    # Create while loops for each type of ship
    # Generate random row, column and direction numbers
    # Create a tuple for the randomly generated ship
    # If the ship is legal (i.e. it satisfies ok_to_place_ship_at) then append it to the fleet list with the function place_ship_at
    # If it does not satisfy ok_to_place_ship_at, repeat the while loop until there is the required number of each type of ship
    # Return the fleet once all four while loops have been completed                                 
    while battleships == False:
      row = random.randint(0,9)       
      column = random.randint(0,9)    
      horizontal = random.randint(0,1) 
      if horizontal == 0:
        horizontal = True
      elif horizontal == 1:
        horizontal = False
      ship = tuple((row, column, horizontal, 4, set()))
      if ok_to_place_ship_at(row, column, horizontal, 4, fleet) == True:
          place_ship_at(row, column, horizontal, 4, fleet)
      if len(fleet) == 1:
        battleships = True

    while cruisers == False:             
      row = random.randint(0,9)       
      column = random.randint(0,9)    
      direction = random.randint(0,1) 
      if horizontal == 0:
        horizontal = True
      elif horizontal == 1:
        horizontal = False
      ship = tuple((row, column, horizontal, 3, set()))
      if ok_to_place_ship_at(row, column, horizontal, 3, fleet) == True:
          place_ship_at(row, column, horizontal, 3, fleet)
      if len(fleet) == 3:
        cruisers = True

    while destroyers == False:
      row = random.randint(0,9)       
      column = random.randint(0,9)    
      direction = random.randint(0,1) 
      if horizontal == 0:
        horizontal = True
      elif horizontal == 1:
        horizontal = False
      ship = tuple((row, column, horizontal, 2, set()))
      if ok_to_place_ship_at(row, column, horizontal, 2, fleet) == True:
          place_ship_at(row, column, horizontal, 2, fleet)
      if len(fleet) == 6:
        destroyers = True

    while submarines == False:
      row = random.randint(0,9)       
      column = random.randint(0,9)    
      direction = random.randint(0,1) 
      if horizontal == 0:
        horizontal = True
      elif horizontal == 1:
        horizontal = False
      ship = tuple((row, column, horizontal, 1, set()))
      if ok_to_place_ship_at(row, column, horizontal, 1, fleet) == True:
          place_ship_at(row, column, horizontal, 1, fleet)
      if len(fleet) == 10:
        submarines = True
    
    return fleet    

def check_if_hits(row, column, fleet):
    '''Returns Boolean value, which is True if the shot of the human player
    at the square represented by row and column hits any of the ships of fleet, and False otherwise.'''
    # Generate list of occupied cells
    # Generate tuple of target cell from arguments provided to function
    # Using the in keyword, determine whether the target cell is in the list of occupied cells and return a Boolean
    occupied_cells = []
    target_cell = tuple((row, column))
    for s in range(len(fleet)):
        occupied_cells.append(tuple((fleet[s][0], fleet[s][1])))
        if fleet[s][2] == True:
            for i in range(1, fleet[s][3]):
                cell = tuple((fleet[s][0], fleet[s][1]+i))
                occupied_cells.append(cell)

        elif fleet[s][2] == False:
            for i in range(1, fleet[s][3]):
                cell = tuple((fleet[s][0]+i, fleet[s][1]))
                occupied_cells.append(cell)

    return target_cell in occupied_cells

def hit(row, column, fleet):
    '''Returns a tuple (fleet1, ship) where ship is the ship from the fleet fleet that receives a hit
    by the shot at the square represented by row and column, and fleet1 is the fleet resulting from this hit.
    It may be assumed that shooting at the square row, column results in hitting of some ship in fleet.
    Note that ship must represent the ship after the hit.'''
    # Generate list of occupied cells, modified to be a list of lists of squares occupied by individual ships
    occupied_cells = []
    hit_cell = tuple((row, column))
    new_ship = ""
    fleet1 = fleet
    for s in range(len(fleet)):
        ship_squares = []
        ship_squares.append(tuple((fleet[s][0], fleet[s][1])))
        if fleet[s][2] == True:
            for i in range(1, fleet[s][3]):
                cell = tuple((fleet[s][0], fleet[s][1]+i))
                ship_squares.append(cell)
        elif fleet[s][2] == False:
            for i in range(1, fleet[s][3]):
                cell = tuple((fleet[s][0]+i, fleet[s][1]))
                ship_squares.append(cell)
        occupied_cells.append(ship_squares)

    # Determine which ship is affected by hit_cell
    # Add co-ordinates represented by hit_cell to set of squares hit in affected ship
    # If the ship is now sunk (indicated by is_sunk function), rmeove ship from fleet
    # Return both the updated fleet (reflecting the affected ship's hit specified by hit_cell), and the updated ship itself
    for i in range(len(occupied_cells)):
      if hit_cell in occupied_cells[i]:
        list_ship = list(fleet1[i])
        list_ship[4].add(hit_cell)
        new_ship = tuple((list_ship))
        if is_sunk(new_ship) == True:
            fleet1.remove(fleet1[i])
        else:
            fleet1[i] = new_ship

    return tuple((fleet1, new_ship))
    
def are_unsunk_ships_left(fleet):
    '''Returns Boolean value, which is True if there are ships in the fleet that are still not sunk, and False otherwise.'''
    # Return Boolean determining whether the length of the fleet list is greater than 0
    # Return True if len(fleet) > 0 (meaning there are still unsunk ships left), and False if len(fleet) = 0 (meaning all ships have been sunk)
    return len(fleet) > 0
    
def main():
    '''Returns nothing. It prompts the user to call out rows and columns of shots and outputs the responses
    of the computer (see General Idea of Assignment) iteratively until the game stops. Our expectations from this function:
    (a) there must be an option for the human player to quit the game at any time,
    (b) the program must never crash (i.e., no termination with Python error messages), whatever the human player does.
    Note that there is an indicative implementation of main() to help you start working,
    but it does not satisfy the expectations above and you should improve or entirely redo it.'''
    # Randomly set board using function randomly_place_all_ships
    # Create an empty list_of_hits
    # Set game_over to False and counter of shots to 0
    current_fleet = randomly_place_all_ships()
    list_of_hits = []

    game_over = False
    shots = 0

    print("The fleet consists of 10 ships. The fleet is made up of 4 different types of ships, each of different size as follows:")
    print("- One battleship, occuping four squares")
    print("- Two cruisers, occuping three squares each")
    print("- Three destroyers, occupying two squares each")
    print("- Four submarines, occupying one square each.")
    print("There is clear water separating all the ships in the fleet. Sink all the ships in the fleet in as few shots as possible. Good luck!")

    # Begin a while loop asking for user input of rows and columns, with option to quit in each turn
    # Cast user input as a list
    # Ensure that input is legal (i.e. two integers between 0 and 9 inclusive), and handle exceptions if input is not legal
    # If row and column has already been hit, let the user know
    # If the rest of the code runs, the input is legal and represents a new cell being targeted
    while not game_over:
        user_input = input("Enter row and column to shoot (separated by space), or 'q' to quit: ").split()
        try:
            int(user_input[0])
            int(user_input[1])
            if int(user_input[0]) >= 0 and int(user_input[0]) <= 9 and int(user_input[1]) >= 0 and int(user_input[1]) <= 9 and len(user_input) ==2:
                pass
            elif len(user_input) > 2:
                print("Please enter two values only.")
                continue
            elif int(user_input[0]) > 9 or int(user_input[1]) > 9 or int(user_input[0]) < 0 or int(user_input[1]) < 0:
                print("Row and column numbers cannot be out of bounds, please try again.")
                continue
        except IndexError:
            print("Invalid input, please try again.")
            continue
        except:
            if user_input[0].lower() == "q":
                game_over = True
                print("You have quit the game. You used",shots,"shots.")
                break
            elif not user_input:
                print("Invalid input, please try again.")
                continue
            else:
                print("Invalid input, please try again.")
                continue
        current_row = int(user_input[0])
        current_column = int(user_input[1])
        if tuple((current_row, current_column)) in list_of_hits:
            print("You have already hit this square, please try again.")
            continue
        shots += 1

    # If a ship in the fleet is hit (using function check_if_hits), append hit cell to list_of_hits, update fleet (using function hit) and inform user
    # If a ship has been sunk (determined using function is_sunk), inform user
    # If the user has missed, append hit cell to list_of_hits and inform user
    # For every turn, check whether there are any unsunk ships left (using function are_unsunk_ships_left)
    # If True, return to start of loop, else game_over = True and inform user of number of shots required
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            list_of_hits.append(tuple((current_row, current_column)))
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")
            list_of_hits.append(tuple((current_row, current_column)))

        if not are_unsunk_ships_left(current_fleet):
            game_over = True
            print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
