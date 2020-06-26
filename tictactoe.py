def print_board(cells):
    print("-" * 9)
    coord_list = []
    for i in range(0, 9, 3):
        # Print the game board
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
        # Break into nested lists to mirror 3x3 game board
        coord_list += [[cells[i], cells[i + 1], cells[i + 2]]]
    print("-" * 9)
    coord_list.reverse()  # Reverse nested lists in order to mirror table of coordinates
    return coord_list


def create_lists(cells):
    rows = [cells[i : i + 3] for i in range(0, 9, 3)]
    columns = [cells[i::3] for i in range(0, 3)]
    tl_diagonal = [cells[0::4]]
    tr_diagonal = [cells[2:8:2]]
    all_combinations = rows + columns + tl_diagonal + tr_diagonal
    return all_combinations, rows


def resolve_state(board_state):
    flat_board = [item for sublist in board_state for item in sublist]
    all_cells = [",".join(nested_list) for nested_list in board_state]
    combinations = [nested_list.replace(",", "") for nested_list in all_cells]
    if "XXX" in combinations:
        print("X wins")
        return False
    if "OOO" in combinations:
        print("O wins")
        return False
    if " " in flat_board:
        return True
    if " " not in flat_board:
        print("Draw")
        return False


def make_move(coordinates, player):
    while True:
        occupied = ["X", "O"]
        try:
            user_move = [
                int(place) for place in input("Enter the coordinates: ").split()
            ]
        except ValueError:
            print("You should only enter numbers!")
            make_move(coordinates, player)
        else:
            if user_move[0] > 3 or user_move[1] > 3:
                print("Coordinates should be from 1 to 3!")
                make_move(coordinates, player)
            elif coordinates[user_move[1] - 1][user_move[0] - 1] in occupied:
                print("This cell is occupied! Choose another one!")
                make_move(coordinates, player)
            else:
                coordinates[user_move[1] - 1][user_move[0] - 1] = player
                coordinates.reverse()
                flattened = [val for sublist in coordinates for val in sublist]
                coordinates.reverse()
                print_board(flattened)
                combinations, rows = create_lists(flattened)
                flag = resolve_state(combinations)
                if flag:
                    if player == "X":
                        player = "O"
                    elif player == "O":
                        player = "X"
                    make_move(coordinates, player)
            break


starting_board = " " * 9
player = "X"
coordinates = print_board(starting_board)
make_move(coordinates, player)
