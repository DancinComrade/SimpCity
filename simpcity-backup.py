import csv
import random

"""
Tan Kai Zhe - P06 - 9/8/2021

Advanced:
- Finished Program Validation
- Finished High Scores

Additional Features:
- Remaining Buildings at the Side

TO-DO:
1) additional feature: display remaining buildings at the side
2) Add necessary comments for documentation
"""

# Main menu
def print_menu():
    print("Welcome, mayor of Simp City!")
    print("----------------------------")
    while True:
        try:
            option = int(input("1. Start new game\n2. Load saved game\n3. Show high scores\n\n0. Exit\nYour choice? "))
            return option
        except:
            print("Error: Please enter a number")
            pass

# Start new game by generating a fresh blank 4x4 board
def new_game():
    # create new 4x4 board
    row = 4
    col = 4
    board = []
    # Creates nested list with 0
    #[[0,0,0,0],
    # [0,0,0,0],
    # [0,0,0,0],
    # [0,0,0,0]]
    for i in range(row):
        board.append([])
        for n in range(col):
            board[i].append("   ")

    # choose building randomly from building list
    building_dict = {"BCH":8, "FAC":8, "HSE": 8, "SHP": 8, "HWY": 8}
    building_list = []

    building1 = random.choice(list(building_dict.keys()))
    building2 = random.choice(list(building_dict.keys()))

    count = 1
    print("Turn {}".format(count))
    generate_board(board, building_dict)
    
    while True:
        try:
            option = int(input("1. Build a {}\n2. Build a {}\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\nYour choice?".format(building1, building2)))
            break
        except:
            print("Enter a number")

    pos_list = [] 
    while option != 0 and count <= 16:
        if count == 17:
            break
        if option == 1:
            # initialize function build() to ask for position 
            pos_list = build()
            if count > 1:
                # check legal placement
                if check_placement(pos_list[0], pos_list[1], board):
                    # reduce number of building in dictionary by 1
                    building_dict[building1] -= 1
                    board[pos_list[0]][pos_list[1]] = building1
                    count += 1

                else:
                    while check_placement(pos_list[0], pos_list[1], board) != True:
                        print("Illegal placement. Try again")
                        pos_list = build()
                    building_dict[building1] -= 1
                    board[pos_list[0]][pos_list[1]] = building1
                    count += 1

            else:
                building_dict[building1] -= 1
                board[pos_list[0]][pos_list[1]] = building1
                count += 1

            building_list = []

            for j in building_dict:
                if building_dict[j] != 0:
                    building_list.append(j)

            # Generate building again
            building1 = random.choice(building_list)
            building2 = random.choice(building_list)

        elif option == 2:
            pos_list = build()
            if count > 1:
                if check_placement(pos_list[0], pos_list[1], board):
                    building_dict[building2] -= 1
                    board[pos_list[0]][pos_list[1]] = building2
                    count += 1

                else:
                    while check_placement(pos_list[0], pos_list[1], board) != True:
                        print("Illegal placement. Try again")
                        pos_list = build()
                    building_dict[building2] -= 1
                    board[pos_list[0]][pos_list[1]] = building2
                    count += 1

            else:
                building_dict[building2] -= 1
                board[pos_list[0]][pos_list[1]] = building2
                count += 1

            building_list = []

            for j in building_dict:
                if building_dict[j] != 0:
                    building_list.append(j)

            # Generate building again
            building1 = random.choice(building_list)
            building2 = random.choice(building_list)

        elif option == 3:
            remaining_buildings(building_dict)

        elif option == 4:
            score(board)

        elif option == 5:
            confirmation = input("Saving the current state of game will overwrite the previous save file. Do you want to continue? [Y/n] ")
            if str.lower(confirmation) == "y":
                save_game(board, building_dict, count)
                print("Game state saved as save.csv")
            else:
                print("Game not saved.")
        if count == 17:
            print("Final layout of Simp City:")
            generate_board(board, building_dict)
            break
        print("Turn {}".format(count))    

        generate_board(board, building_dict)

        while True:
            try:
                option = int(input("1. Build a {}\n2. Build a {}\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\nYour choice?".format(building1, building2)))
                break
            except:
                print("Error: Enter a number")
    if option != 0:
        usr_score = score(board)
        high_scores(usr_score)
        start()
    elif option == 0:
        start()


# Load game from save file, if doesn't exist, prompt save doesn't exist and exit to menu
def load_game():
    if load_save():
        # Execute load_save() to get necessary variables: board and dict
        board = load_save()[0]
        building_dict = load_save()[1]
        count = int(load_save()[2])
        building_list = []

        for j in building_dict:
            if building_dict[j] != 0:
                building_list.append(j)

        # Generate building again
        building1 = random.choice(building_list)
        building2 = random.choice(building_list)
        print("Turn {}".format(count))
        generate_board(board, building_dict)

        while True:
            try:
                option = int(input("1. Build a {}\n2. Build a {}\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\nYour choice?".format(building1, building2)))
                break
            except:
                print("Error: Enter a number")

        pos_list = []
        while option != 0 and count <= 16:
            if count == 17:
                break
            if option == 1:
                # initialize function build() to ask for position
                pos_list = build()
                if count > 1:
                    # check legal placement
                    if check_placement(pos_list[0], pos_list[1], board):
                        # reduce number of building in dictionary by 1
                        building_dict[building1] -= 1
                        board[pos_list[0]][pos_list[1]] = building1
                        count += 1

                    else:
                        while check_placement(pos_list[0], pos_list[1], board) != True:
                            print("Illegal placement. Try again")
                            pos_list = build()
                        building_dict[building1] -= 1
                        board[pos_list[0]][pos_list[1]] = building1
                        count += 1

                else:
                    building_dict[building1] -= 1
                    board[pos_list[0]][pos_list[1]] = building1
                    count += 1

                building_list = []

                for j in building_dict:
                    if building_dict[j] != 0:
                        building_list.append(j)

                # Generate building again
                building1 = random.choice(building_list)
                building2 = random.choice(building_list)

            elif option == 2:
                pos_list = build()
                if count > 1:
                    if check_placement(pos_list[0], pos_list[1], board):
                        building_dict[building2] -= 1
                        board[pos_list[0]][pos_list[1]] = building2
                        count += 1

                    else:
                        while check_placement(pos_list[0], pos_list[1], board) != True:
                            print("Illegal placement. Try again")
                            pos_list = build()
                        building_dict[building2] -= 1
                        board[pos_list[0]][pos_list[1]] = building2
                        count += 1

                else:
                    building_dict[building2] -= 1
                    board[pos_list[0]][pos_list[1]] = building2
                    count += 1

                building_list = []

                for j in building_dict:
                    if building_dict[j] != 0:
                        building_list.append(j)

                # Generate building again
                building1 = random.choice(building_list)
                building2 = random.choice(building_list)

            elif option == 3:
                remaining_buildings(building_dict)

            elif option == 4:
                score(board)

            elif option == 5:
                confirmation = input("Saving the current state of game will overwrite the previous save file. Do you want to continue? [Y/n] ")
                if str.lower(confirmation) == "y":
                    save_game(board, building_dict, count)
                    print("Game state saved as save.csv")
                else:
                    print("Game not saved.")
            if count == 17:
                print("Final layout of Simp City:")
                generate_board(board, building_dict)
                break

            print("Turn {}".format(count))

            generate_board(board, building_dict)

            while True:
                try:
                    option = int(input("1. Build a {}\n2. Build a {}\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\nYour choice?".format(building1, building2)))
                    break
                except:
                    print("Error: Enter a number")
        if option != 0:
            usr_score = score(board)
            high_scores(usr_score)
            start()
        elif option == 0:
            start()
    else:
        print("Save file not found.")
        start()


# Check orthogonally adjacent, if true returns true and vice versa
def check_placement(row, col, board):
    """
    row and col to know the location of item to check in list,
    get the current board to know location of all items

    [row-1,col-1] [row-1, col ] [row-1,col+1]
    [ row ,col-1] [ row , col ] [ row ,col+1]
    [row+1,col-1] [row+1, col ] [row+1,col+1]
    """
    # board[row][col] -> the location of the item to check
    # check building type as each building type has diff rules
    
    # 1st check if position of item has existing building or not
    if board[row][col] == "BCH" or board[row][col] == "FAC" or board[row][col] == "HSE" or board[row][col] == "SHP" or board[row][col] == "HWY":
        # if have, return False
        return False
    else:
        if row == 3:
            if col == 3:
                # Don't check right and below
                if board[row-1][col] == "BCH" or board[row-1][col] == "FAC" or board[row-1][col] == "HSE" or board[row-1][col] == "SHP" or board[row-1][col] == "HWY": 
                    return True 
                elif board[row][col-1] == "BCH" or board[row][col-1] == "FAC" or board[row][col-1] == "HSE" or board[row][col-1] == "SHP" or board[row][col-1] == "HWY": 
                    return True
            elif col == 0:
                # Don't check left and below
                if board[row-1][col] == "BCH" or board[row-1][col] == "FAC" or board[row-1][col] == "HSE" or board[row-1][col] == "SHP" or board[row-1][col] == "HWY":
                    return True
                elif board[row][col+1] == "BCH" or board[row][col+1] == "FAC" or board[row][col+1] == "HSE" or board[row][col+1] == "SHP" or board[row][col+1] == "HWY": 
                    return True
                
            else:
                # For all other cells at row 3, don't check below
                if board[row-1][col] == "BCH" or board[row-1][col] == "FAC" or board[row-1][col] == "HSE" or board[row-1][col] == "SHP" or board[row-1][col] == "HWY": 
                    return True 
                elif board[row][col-1] == "BCH" or board[row][col-1] == "FAC" or board[row][col-1] == "HSE" or board[row][col-1] == "SHP" or board[row][col-1] == "HWY": 
                    return True
                elif board[row][col+1] == "BCH" or board[row][col+1] == "FAC" or board[row][col+1] == "HSE" or board[row][col+1] == "SHP" or board[row][col+1] == "HWY": 
                    return True
        elif row == 0:
            if col == 3:
                # Don't check up and right
                if board[row+1][col] == "BCH" or board[row+1][col] == "FAC" or board[row+1][col] == "HSE" or board[row+1][col] == "SHP" or board[row+1][col] == "HWY":
                    return True
                elif board[row][col-1] == "BCH" or board[row][col-1] == "FAC" or board[row][col-1] == "HSE" or board[row][col-1] == "SHP" or board[row][col-1] == "HWY": 
                    return True
            elif col == 0:
                if board[row+1][col] == "BCH" or board[row+1][col] == "FAC" or board[row+1][col] == "HSE" or board[row+1][col] == "SHP" or board[row+1][col] == "HWY":
                    return True
                elif board[row][col+1] == "BCH" or board[row][col+1] == "FAC" or board[row][col+1] == "HSE" or board[row][col+1] == "SHP" or board[row][col+1] == "HWY": 
                    return True
            else:
                # Don't check up
                if board[row+1][col] == "BCH" or board[row+1][col] == "FAC" or board[row+1][col] == "HSE" or board[row+1][col] == "SHP" or board[row+1][col] == "HWY":
                    return True
                elif board[row][col-1] == "BCH" or board[row][col-1] == "FAC" or board[row][col-1] == "HSE" or board[row][col-1] == "SHP" or board[row][col-1] == "HWY": 
                    return True
                elif board[row][col+1] == "BCH" or board[row][col+1] == "FAC" or board[row][col+1] == "HSE" or board[row][col+1] == "SHP" or board[row][col+1] == "HWY": 
                    return True
        elif col == 3:
            # Don't check right
            if board[row-1][col] == "BCH" or board[row-1][col] == "FAC" or board[row-1][col] == "HSE" or board[row-1][col] == "SHP" or board[row-1][col] == "HWY": 
                return True 
            elif board[row+1][col] == "BCH" or board[row+1][col] == "FAC" or board[row+1][col] == "HSE" or board[row+1][col] == "SHP" or board[row+1][col] == "HWY":
                return True
            elif board[row][col-1] == "BCH" or board[row][col-1] == "FAC" or board[row][col-1] == "HSE" or board[row][col-1] == "SHP" or board[row][col-1] == "HWY": 
                return True
        elif col == 0:
            # Don't check left
            if board[row-1][col] == "BCH" or board[row-1][col] == "FAC" or board[row-1][col] == "HSE" or board[row-1][col] == "SHP" or board[row-1][col] == "HWY": 
                return True 
            elif board[row+1][col] == "BCH" or board[row+1][col] == "FAC" or board[row+1][col] == "HSE" or board[row+1][col] == "SHP" or board[row+1][col] == "HWY":
                return True
            elif board[row][col+1] == "BCH" or board[row][col+1] == "FAC" or board[row][col+1] == "HSE" or board[row][col+1] == "SHP" or board[row][col+1] == "HWY": 
                return True
        else:
            if board[row+1][col] == "BCH" or board[row+1][col] == "FAC" or board[row+1][col] == "HSE" or board[row+1][col] == "SHP" or board[row+1][col] == "HWY":
                return True
            elif board[row-1][col] == "BCH" or board[row-1][col] == "FAC" or board[row-1][col] == "HSE" or board[row-1][col] == "SHP" or board[row-1][col] == "HWY": 
                return True 
            elif board[row][col-1] == "BCH" or board[row][col-1] == "FAC" or board[row][col-1] == "HSE" or board[row][col-1] == "SHP" or board[row][col-1] == "HWY": 
                return True
            elif board[row][col+1] == "BCH" or board[row][col+1] == "FAC" or board[row][col+1] == "HSE" or board[row][col+1] == "SHP" or board[row][col+1] == "HWY": 
                return True
        

# Generate board with location of building, and remaining buildings at the side
def generate_board(board, building_dict):
    # Takes board as argument
    # Print out the board
    num_columns = len(board[0])
    num_rows = len(board)

    print("  ", " A ", "  ", " B ", "  ", " C ", "  ", " D ", "       ", "Building        Remaining")

    for col in range(num_columns):
        if col == 0:
            print("  ", end="")
        print(("+------"), end="")
    print("+     --------        ---------")

    # Loop through building_dict and display keys and values to form a table
    for row in range(num_rows):
        print(row + 1, end="")
        for col in board[row]:
            print(" | {}".format(col), end=" ")
        if row == 0:
            print(" |     {:<16}{}".format("BCH",building_dict["BCH"]))
        elif row == 1:
            print(" |     {:<16}{}".format("HSE", building_dict["HSE"]))
        elif row == 2:
            print(" |     {:<16}{}".format("HWY", building_dict["HWY"]))
        else:
            print(" |")

        for col in range(num_columns):
            if col == 0:
                print("  ", end="")
            print("+------", end="")
        if row == 0:
            print("+     {:<16}{}".format("FAC", building_dict["FAC"]))
        elif row == 1:
            print("+     {:<16}{}".format("SHP", building_dict["SHP"]))
        else:
            print("+")


# Load game variables (eg. num of turns, location of building (in a list) and remaining buildings from save.csv
def load_save():
    try:
        with open("save.csv", "r") as file:
            # Read everything from csv
            reader = csv.reader(file)
            # Convert the data read to a list
            data = list(reader)

            # Cleaning the list to remove empty list (which is due to \n) and append
            # cleaned list to new list, board_list (which contains position of buildings)
            board_list = []
            for row in data[:7+1]:
                if row != []:
                    board_list.append(row)

            # Loop from data[8:] onwards which is the section for dictionary
            # Split the string in half by the ":"
            # Assign respective keys and values to bulding dict
            building_dict = {}
            for row in data[8:-1]:
                for col in row:
                    col = col.split(":")
                    building_dict[col[0]] = int(col[1])

            count = data[-1][0]

        return board_list, building_dict, count
    except:
        return None


# Save game variables for future use
def save_game(board, dictionary, count):
    # use with statement as recommended by python for better exception handling and also
    # no need to file.close() as with will do it automatically
    with open("save.csv", "w") as file:
        # seek the start of tile file (first line)
        file.seek(0)
        # Write board list (position of buildings) to csv
        csvwriter = csv.writer(file, delimiter=",")
        csvwriter.writerows(board)
        # Write building_dict which contains the number of building left to csv
        """
        headers = ["Building", "Count"]
        csv_dict = csv.DictWriter(file, fieldnames=headers)
        for data in dictionary:
            csv_dict.writerow(data)
        """
        """
        for row in range(len(board)):
            for col in range(len(board[row])):
                if type(board[row][col]) == type(""):
                    board[row][col] == "0"
                    file.write("{}".format(board[row][col]))
                else:
                    file.write("{}".format(board[row][col]))
        """
        for key, values in dictionary.items():
            file.write("{}:{}\n".format(key,values))

        file.write(str(count))
        file.truncate


# Returns [row][col] of the location of the building, for appending to list (eg. Translating "A1" to 0,0)
def build():
    # Get position from user and return two num values (row, col)
    while True:    
        location = input("Build where? (Eg. A1) ")
        location = str.upper(location)
        if len(location) == 2 and (location[0] == "A" or location[0] == "B" or location[0] == "C" or location[0] == "D") and (location[1] == "1" or location[1] == "2" or location[1] == "3" or location[1] == "4"):
            break
        else:
            print("Error: Enter a in the following format: [letter][number]\nExample: A1 or a1")
    # convert input to uppercase
    if location == "A1":
        return 0,0
    elif location == "B1":
        return 0,1
    elif location == "C1":
        return 0,2          
    elif location == "D1":
        return 0,3
    elif location == "A2":
        return 1,0
    elif location == "B2":
        return 1,1
    elif location == "C2":
        return 1,2          
    elif location == "D2":
        return 1,3
    elif location == "A3":
        return 2,0
    elif location == "B3":
        return 2,1
    elif location == "C3":
        return 2,2          
    elif location == "D3":
        return 2,3
    elif location == "A4":
        return 3,0
    elif location == "B4":
        return 3,1
    elif location == "C4":
        return 3,2          
    elif location == "D4":
        return 3,3


# Display remaining building (Rendered obsolete with the additional feature of always display remaining buildings)
def remaining_buildings(building_dict):
    print("Building        Remaining")
    print("--------        ---------")
    # Loop through building_dict and display keys and values to form a table
    for key in building_dict:
        print("{}{:>14}".format(key, building_dict[key]))


# Calculate total score of game by taking the location of building in nested list as argument
def score(board):
    # Lists to store scores of each building
    bch = []
    fac = []
    hse = []
    shp = []
    hwy = []

    for row in range(len(board)):
        # if col A append 3
        if "BCH" in board[row][0]:
            bch.append(3)
        # if col D append 3
        if "BCH" in board[row][3]:
            bch.append(3)
        if "BCH" in board[row][1]:
            bch.append(1)
        if "BCH" in board[row][2]:
            bch.append(1)
        
        for col in range((len(board[row]))):
            if board[row][col] == "FAC":
                # count the num of factory and reassign value
                fac.append(1)
        
    # Factories: Get count of factories and do conversion        
    if sum(fac) <= 4:
        for i in range(len(fac)):
            if fac[i] == 1:
                fac[i] = len(fac)
    elif sum(fac) > 4:
        for i in range(0,4):
            if fac[i] == 1:
                fac[i] = 4  

                
    """
    row and col to know the location of item to check in list,
    get the current board to know location of all items

    [row-1,col-1] [row-1, col ] [row-1,col+1]
    [ row ,col-1] [ row , col ] [ row ,col+1]
    [row+1,col-1] [row+1, col ] [row+1,col+1]
    """
    # House
    #     0 1 2 3
    # 0 [[0,0,0,0], board[row][col]
    # 1 [0,0,0,0],
    # 2 [0,0,0,0],
    # 3 [0,0,0,0]]
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "HSE":
                temp_list = []
                if row == 3:
                    if col == 3:
                        # Check up and left
                        if board[row-1][col] == "FAC" or board[row][col-1] == "FAC":
                            hse.append(1)
                        elif board[row-1][col] == "   " and board[row][col-1] == "   ":
                            hse.append(1)
                        else:
                            if board[row-1][col] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col-1] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col] == "BCH":
                                temp_list.append(2)
                            if board[row][col-1] == "BCH":
                                temp_list.append(2)

                            # At the end of check, sum temp_list, append to hse list
                            hse.append(sum(temp_list))

                    elif col == 0:
                        # Check up and right
                        if board[row-1][col] == "FAC" or board[row][col+1] == "FAC":
                            hse.append(1)
                        elif board[row-1][col] == "   " and board[row][col+1] == "   ":
                            hse.append(1)
                        else:
                            if board[row-1][col] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col+1] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col] == "BCH":
                                temp_list.append(2)
                            if board[row][col+1] == "BCH":
                                temp_list.append(2)

                            # At the end of check, sum temp_list, append to hse list
                            hse.append(sum(temp_list))

                    else:
                        # For all other cells at row 3, don't check below
                        if board[row-1][col] == "FAC" or board[row][col+1] == "FAC" or board[row][col-1] == "FAC":
                            hse.append(1)
                        elif board[row-1][col] == "   " and board[row][col-1] == "   " and board[row][col+1] == "   ":
                            hse.append(1)
                        else:
                            if board[row-1][col] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col+1] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col-1] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col] == "BCH":
                                temp_list.append(2)
                            if board[row][col+1] == "BCH":
                                temp_list.append(2)
                            if board[row][col-1] == "BCH":
                                temp_list.append(2)

                            # At the end of check, sum temp_list, append to hse list
                            hse.append(sum(temp_list))

                elif row == 0:
                    if col == 3:
                        # Check bottom and left
                        if board[row+1][col] == "FAC" or board[row][col-1] == "FAC":
                            hse.append(1)
                        elif board[row+1][col] == "   " and board[row][col-1] == "   ":
                            hse.append(1)
                        else:
                            if board[row+1][col] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col-1] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row+1][col] == "BCH":
                                temp_list.append(2)
                            if board[row][col-1] == "BCH":
                                temp_list.append(2)

                            # At the end of check, sum temp_list, append to hse list
                            hse.append(sum(temp_list))

                    elif col == 0:
                        # Check bottom and right
                        if board[row+1][col] == "FAC" or board[row][col+1] == "FAC":
                            hse.append(1)
                        elif board[row+1][col] == "   " and board[row][col+1] == "   ":
                            hse.append(1)
                        else:
                            if board[row+1][col] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col+1] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row+1][col] == "BCH":
                                temp_list.append(2)
                            if board[row][col+1] == "BCH":
                                temp_list.append(2)

                            # At the end of check, sum temp_list, append to hse list
                            hse.append(sum(temp_list))

                    else:
                        # Don't check up
                        if board[row+1][col] == "FAC" or board[row][col+1] == "FAC" or board[row][col-1] == "FAC":
                            hse.append(1)
                        elif board[row+1][col] == "   " and board[row][col+1] == "   " and board[row][col-1] == "   ":
                            hse.append(1)
                        else:
                            if board[row+1][col] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col+1] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row][col-1] in ("HSE", "SHP"):
                                temp_list.append(1)
                            if board[row+1][col] == "BCH":
                                temp_list.append(2)
                            if board[row][col+1] == "BCH":
                                temp_list.append(2)
                            if board[row][col-1] in "BCH":
                                temp_list.append(2)

                            # At the end of check, sum temp_list, append to hse list
                            hse.append(sum(temp_list))

                elif col == 3:
                    # Don't check right
                    if board[row+1][col] == "FAC" or board[row-1][col] == "FAC" or board[row][col-1] == "FAC":
                        hse.append(1)
                    elif board[row + 1][col] == "   " and board[row-1][col] == "   " and board[row][col-1] == "   ":
                        hse.append(1)
                    else:
                        if board[row+1][col] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row-1][col] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row][col-1] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row+1][col] == "BCH":
                            temp_list.append(2)
                        if board[row-1][col] == "BCH":
                            temp_list.append(2)
                        if board[row][col-1] in "BCH":
                            temp_list.append(2)

                        # At the end of check, sum temp_list, append to hse list
                        hse.append(sum(temp_list))

                elif col == 0:
                    # Don't check left
                    if board[row+1][col] == "FAC" or board[row-1][col] == "FAC" or board[row][col+1] == "FAC":
                        hse.append(1)
                    elif board[row+1][col] == "   " and board[row-1][col] == "   " and board[row][col+1] == "   ":
                        hse.append(1)
                    else:
                        if board[row+1][col] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row-1][col] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row][col+1] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row+1][col] == "BCH":
                            temp_list.append(2)
                        if board[row-1][col] == "BCH":
                            temp_list.append(2)
                        if board[row][col+1] in "BCH":
                            temp_list.append(2)

                        # At the end of check, sum temp_list, append to hse list
                        hse.append(sum(temp_list))

                else:
                    if board[row+1][col] == "FAC" or board[row-1][col] == "FAC" or board[row][col-1] == "FAC" or board[row][col+1] == "FAC":
                        hse.append(1)
                    elif board[row+1][col] == "   " and board[row-1][col] == "   " and board[row][col-1] == "   " and [row][col+1] == "   ":
                        hse.append(1)
                    else:
                        if board[row+1][col] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row-1][col] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row][col+1] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row][col-1] in ("HSE", "SHP"):
                            temp_list.append(1)
                        if board[row+1][col] == "BCH":
                            temp_list.append(2)
                        if board[row-1][col] == "BCH":
                            temp_list.append(2)
                        if board[row][col+1] in "BCH":
                            temp_list.append(2)
                        if board[row][col-1] in "BCH":
                            temp_list.append(2)

                        # At the end of check, sum temp_list, append to hse list
                        hse.append(sum(temp_list))

    # Shop
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "SHP":
                temp_list = []
                ref_list = []
                if row == 3:
                    if col == 3:
                        # Check up and left
                        if board[row - 1][col] == "   " and board[row][col - 1] == "   " and board[row - 1][
                            col] not in ref_list and board[row][col - 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row - 1][col])
                        else:
                            if board[row - 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row - 1][
                                col] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row - 1][col])
                            if board[row][col - 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                                col - 1] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row][col - 1])

                        # At the end of check, sum temp_list, append to hse list
                        shp.append(sum(temp_list))

                    elif col == 0:
                        # Check up and right
                        if board[row - 1][col] == "   " and board[row][col + 1] == "   " and board[row - 1][
                            col] not in ref_list and board[row][col + 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row - 1][col])
                        else:
                            if board[row - 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row - 1][
                                col] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row - 1][col])
                            if board[row][col + 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                                col + 1] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row][col + 1])

                        # At the end of check, sum temp_list, append to hse list
                        shp.append(sum(temp_list))

                    else:
                        # For all other cells at row 3, don't check below
                        if board[row - 1][col] == "   " and board[row][col + 1] == "   " and board[row][
                            col - 1] == "   " and board[row - 1][col] not in ref_list and board[row][
                            col + 1] not in ref_list and board[row][col - 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row - 1][col])
                        else:
                            if board[row - 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row - 1][
                                col] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row - 1][col])
                            if board[row][col + 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                                col + 1] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row][col + 1])
                            if board[row][col - 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                                col - 1] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row][col - 1])

                        # At the end of check, sum temp_list, append to hse list
                        shp.append(sum(temp_list))

                elif row == 0:
                    if col == 3:
                        # Check bottom and left
                        if board[row + 1][col] == "   " and board[row][col - 1] == "   " and board[row + 1][
                            col] not in ref_list and board[row][col - 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row - 1][col])
                        else:
                            if board[row + 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row + 1][
                                col] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row + 1][col])
                            if board[row][col - 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                                col - 1] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row][col - 1])

                        # At the end of check, sum temp_list, append to hse list
                        shp.append(sum(temp_list))

                    elif col == 0:
                        # Check bottom and right
                        if board[row + 1][col] == "   " and board[row][col + 1] == "   " and board[row + 1][
                            col] not in ref_list and board[row][col + 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row - 1][col])
                        else:
                            if board[row + 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row + 1][
                                col] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row + 1][col])
                            if board[row][col + 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                                col + 1] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row][col + 1])

                        # At the end of check, sum temp_list, append to hse list
                        shp.append(sum(temp_list))

                    else:
                        # Don't check up
                        if board[row + 1][col] == "   " and board[row][col + 1] == "   " and board[row][
                            col - 1] == "   " and board[row + 1][col] not in ref_list and board[row][
                            col + 1] not in ref_list and board[row][col - 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row - 1][col])
                        else:
                            if board[row + 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row + 1][
                                col] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row + 1][col])
                            if board[row][col - 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                                col - 1] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row][col - 1])
                            if board[row][col + 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                                col + 1] not in ref_list:
                                temp_list.append(1)
                                ref_list.append(board[row][col + 1])

                        # At the end of check, sum temp_list, append to hse list
                        shp.append(sum(temp_list))

                elif col == 3:
                    # Don't check right
                    if board[row + 1][col] == "   " and board[row - 1][col] == "   " and board[row][
                        col - 1] == "   " and board[row + 1][col] not in ref_list and board[row - 1][
                        col] not in ref_list and board[row][col - 1] not in ref_list:
                        temp_list.append(1)
                        ref_list.append(board[row - 1][col])
                    else:
                        if board[row + 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row + 1][
                            col] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row + 1][col])
                        if board[row - 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row - 1][
                            col] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row - 1][col])
                        if board[row][col - 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                            col - 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row][col - 1])

                    # At the end of check, sum temp_list, append to hse list
                    shp.append(sum(temp_list))

                elif col == 0:
                    # Don't check left
                    if board[row + 1][col] == "   " and board[row - 1][col] == "   " and board[row][
                        col + 1] == "   " and board[row + 1][col] not in ref_list and board[row - 1][
                        col] not in ref_list and board[row][col + 1] not in ref_list:
                        temp_list.append(1)
                        ref_list.append(board[row - 1][col])
                    else:
                        if board[row + 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row + 1][
                            col] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row + 1][col])
                        if board[row - 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row - 1][
                            col] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row - 1][col])
                        if board[row][col + 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                            col + 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row][col + 1])

                    # At the end of check, sum temp_list, append to hse list
                    shp.append(sum(temp_list))

                else:
                    if board[row + 1][col] == "   " and board[row - 1][col] == "   " and board[row][
                        col + 1] == "   " and board[row][col - 1] == "   " and board[row + 1][col] not in ref_list and \
                            board[row - 1][col] not in ref_list and board[row][col + 1] not in ref_list and board[row][
                        col + 1] not in ref_list:
                        temp_list.append(1)
                        ref_list.append(board[row - 1][col])
                    else:
                        if board[row + 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row + 1][
                            col] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row + 1][col])
                        if board[row - 1][col] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row - 1][
                            col] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row - 1][col])
                        if board[row][col + 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                            col + 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row][col + 1])
                        if board[row][col - 1] in ("HSE", "SHP", "HWY", "BCH", "FAC") and board[row][
                            col - 1] not in ref_list:
                            temp_list.append(1)
                            ref_list.append(board[row][col - 1])

                    # At the end of check, sum temp_list, append to hse list
                    shp.append(sum(temp_list))

    # Highway
    for row in range(len(board)):
        ref_num = 0
        for col in range(len(board[row])):
            if "HWY" in board[row]:
                temp_list = []
                if board[row][col] == "HWY":
                    temp_list.append(1)
                    if col == 0 and ref_num == 0:
                        if board[row][col+1] == "HWY":
                            temp_list.append(1)

                            if board[row][col+2] == "HWY":
                                temp_list.append(1)

                                if board[row][col+3] == "HWY":
                                    temp_list.append(1)

                            else:
                                if board[row][col+3] == "HWY":
                                    temp_list.append(1)

                        else:
                            # Append and clear list
                            for i in range(len(temp_list)):
                                hwy.append(len(temp_list))   

                            temp_list.clear()                  
                            # Skip one block
                            if board[row][col+2] == "HWY":
                                temp_list.append(1)
                                if board[row][col+3] == "HWY":
                                    temp_list.append(1)
                            else:
                                if board[row][col+3] == "HWY":
                                    temp_list.append(1)

                        ref_num += 1
                        for i in range(len(temp_list)):
                            hwy.append(len(temp_list))

                    elif col == 1 and ref_num == 0:
                        if board[row][col+1] == "HWY":
                            temp_list.append(1)

                            if board[row][col+2] == "HWY":
                                temp_list.append(1)

                        else:
                            # Append and clear list
                            for i in range(len(temp_list)):
                                hwy.append(len(temp_list))   

                            temp_list.clear()   
                            # Skip one block
                            if board[row][col+2] == "HWY":
                                temp_list.append(1)
                                
                        ref_num += 1

                        for i in range(len(temp_list)):
                            hwy.append(len(temp_list))

                    elif col == 2 and ref_num == 0:
                        if board[row][col+1] == "HWY":
                            temp_list.append(1)

                        ref_num += 1
                        for i in range(len(temp_list)):
                            hwy.append(len(temp_list))

                    elif col == 3 and ref_num == 0:
                        hwy.append(len(temp_list))
                        ref_num += 1
   
    total = sum(hse) + sum(fac) + sum(shp) + sum(hwy) + sum(bch)

   # Display score menu
    if sum(hse) != 0:
        print("HSE: {} = {}".format(' + '.join(str(x) for x in hse), sum(hse)))
    else:
        print("HSE: 0")
    if sum(fac) != 0:
        print("FAC: {} = {}".format(' + '.join(str(x) for x in fac), sum(fac)))
    else:
        print("FAC: 0")
    if sum(shp) != 0:
        print("SHP: {} = {}".format(' + '.join(str(x) for x in shp), sum(shp)))
    else:
        print("SHP: 0")
    if sum(hwy) != 0:
        print("HWY: {} = {}".format(' + '.join(str(x) for x in hwy), sum(hwy)))
    else:
        print("HWY: 0")
    if sum(bch) != 0:
        print("BCH: {} = {}".format(' + '.join(str(x) for x in bch), sum(bch)))
    else:
        print("BCH: 0")

    print("Total score: {}".format(total))

    return total


# Advanced Feature: Leaderboard
def high_scores(*usr_score):
    # *usr_score (arbitrary argument)
    with open("high_scores.csv", "r") as file:
        # Read everything from csv
        reader = csv.reader(file)
        next(reader, None) # Skip the headers
        # Convert the data read to a list in the format of [[POS, PLAYER, SCORE]]
        data = list(reader)

        # Cleaning the list to remove empty list (which is due to \n) if any, and append
        # cleaned list to new list, score_list (which contains position of buildings)
        score_list = []
        for row in data:
            if row != []:
                score_list.append(row)

    # If *usr_score (arbitrary argument) entered usr_score will return true, else false
    i = 0
    if usr_score:
        count = 0
        count_name = 0
        name_bool = True
        while i < len(score_list):
            # As csv reader, reads from top to bottom of file, starting from highest score 1.,
            # hence it will check everything until it finds one that's smaller than it
            if int(usr_score[0]) > int(score_list[i][2]):
                print("Congratulations! You made the high score board at position {}!".format(int(score_list[i][0])))

                # Validate Input, check for duplicate name inputs/exceeding num of characters
                while True:
                    usr_name = input("Please enter your name (max 20 chars): ")
                    for j in range(len(score_list)):
                        if usr_name in score_list[j]:
                            count_name += 1

                    if count_name != 0:
                        name_bool = False
                    else:
                        name_bool = True

                    count_name = 0
                    if len(usr_name) > 20:
                        print("Username has to be less than 20 characters")
                        pass
                    elif name_bool != True:
                        print("Username already exists.")
                    else:
                        break

                score_list.insert(i, [int(score_list[i][0]), usr_name, int(usr_score[0])])

                pos = 0
                for i in range(len(score_list)):
                    if usr_name in score_list[i]:
                        pos = i

                for i in range(pos + 1, len(score_list)):
                    score_list[i][0] = int(score_list[i][0]) + 1

                print("----------------------- HIGH SCORES -----------------------")
                print("Pos Player                                            Score")
                print("--- ------                                            -----")

                for i in range(len(score_list)):
                    print("{:>2}.".format(score_list[i][0]), end=" ")
                    print("{:<51}".format(score_list[i][1]), end=" ")
                    print("{}".format(score_list[i][2]), end=" ")
                    print()
                print("-----------------------------------------------------------")

                break

            elif int(usr_score[0]) == int(score_list[i][2]):
                for n in range(len(score_list)):
                    count += score_list[n][2].count(str(usr_score[0]))

                # + 1 for under the current position eg. pos 5 + 1, would be pos 6
                print("Congratulations! You made the high score board at position {}!".format(int(score_list[i][0]) + count))
                while True:
                    usr_name = input("Please enter your name (max 20 chars): ")
                    for j in range(len(score_list)):
                        if usr_name in score_list[j]:
                            count_name += 1

                    if count_name != 0:
                        name_bool = False
                    else:
                        name_bool = True

                    count_name = 0
                    if len(usr_name) > 20:
                        print("Username has to be less than 20 characters")
                        pass
                    elif name_bool != True:
                        print("Username already exists.")
                    else:
                        break
                # insert before index
                score_list.insert(i+count, [int(score_list[i][0]) + count, usr_name, int(usr_score[0])])

                pos = 0
                for i in range(len(score_list)):
                    if usr_name in score_list[i]:
                        pos = i

                for i in range(pos + 1, len(score_list)):
                    score_list[i][0] = int(score_list[i][0]) + 1

                print("----------------------- HIGH SCORES -----------------------")
                print("Pos Player                                            Score")
                print("--- ------                                            -----")

                for i in range(len(score_list)):
                    print("{:>2}.".format(score_list[i][0]), end=" ")
                    print("{:<51}".format(score_list[i][1]), end=" ")
                    print("{}".format(score_list[i][2]), end=" ")
                    print()
                print("-----------------------------------------------------------")

                break
            i += 1

    else:
        print("----------------------- HIGH SCORES -----------------------")
        print("Pos Player                                            Score")
        print("--- ------                                            -----")

        for i in range(len(score_list)):
            print("{:>2}.".format(score_list[i][0]), end=" ")
            print("{:<51}".format(score_list[i][1]), end=" ")
            print("{}".format(score_list[i][2]), end=" ")
            print()
        print("-----------------------------------------------------------")

    with open("high_scores.csv", "w") as file:
        # seek the start of tile file (first line)
        file.seek(0)
        field_names = ["Pos", "Player", "Score"]
        # Write board list (position of buildings) to csv
        csvwriter = csv.writer(file, delimiter=",", lineterminator='\n')
        csvwriter.writerow(field_names)
        csvwriter.writerows(score_list)
        # truncate to overwrite existing content in file
        file.truncate


# Start function to initialize the game
def start():
    option = print_menu()
    while option != 0:
        if option == 1:
            new_game()
            break
        elif option == 2:
            load_game()
            break
        elif option == 3:
            high_scores()
            option = print_menu()


# Check if this program is run as a standalone program and not as an imported module
# If so, run the program. Otherwise, don't run.
if __name__ == '__main__':
    start()
    print("Thank you for playing")