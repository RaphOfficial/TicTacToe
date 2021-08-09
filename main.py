class TicTacToe:
    # Vars
    line1 = [None, None, None]
    line2 = [None, None, None]
    line3 = [None, None, None]

    # Lines format: True = O False = X

    def __init__(self):
        pass

    def get_move(self, move_to_get):
        output = None
        all_moves = [self.line1[0], self.line1[1], self.line1[2],
                     self.line2[0], self.line2[1], self.line2[2],
                     self.line3[0], self.line3[1], self.line3[2]]
        if 0 < int(move_to_get) < 10:
            move_to_get = move_to_get - 1
            return all_moves[move_to_get]

        else:
            print('Error: get_move() TicTacToe - move_to_get has to be an integer between 1-0')

    @staticmethod
    def display_empty_grid():
        print('    │   │  ')
        print(' ───┼───┼───')
        print('    │   │  ')
        print(' ───┼───┼───')
        print('    │   │  ')

    def save_a_move(self, player, move):
        # Player is bolean, True for O and False for X
        # Move is an integer, 1-9
        # Vars
        move = int(move) - 1
        current_moves = [
            self.line1,
            self.line2,
            self.line3
        ]
        if -1 < move < 3:
            line = 1
            move = move
        elif 2 < move < 6:
            # Making move in a range 0-2 in the current list self.line
            line = 2
            move = move - 3
        elif 5 < move < 9:
            # Making move in a range 0-2 in the current list self.line
            line = 3
            move = move - 6
        else:
            print('Error: save_a_move class TicTacToe')
            line = 0
            output = -1
            return output

        if line != 0:
            if type(player) == bool:
                line = line - 1
                moves_in_line = current_moves[line]
                if moves_in_line[move] is None:
                    moves_in_line[move] = player
                    current_moves[line] = moves_in_line
                    self.line1 = current_moves[0]
                    self.line2 = current_moves[1]
                    self.line3 = current_moves[2]
                    output = 1
                    return output

                else:
                    output = 0
                    return output

            else:
                print('Error: pick_a_move class TicTacToe Player has to be boolean')
                output = -1
                return output
        # save a move possible outputs:
        # 1 = Move saved successfully
        # 0 = Move is already picked
        # -1 = Unknown error

    def display_grid(self):
        current_pos = 0
        locations = (self.line1, self.line2, self.line3)
        text = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        for line in locations:
            for move in line:
                if type(move) == bool:
                    if move:  # If move is O
                        text[current_pos] = 'O'
                    if not move:  # If move is X
                        text[current_pos] = 'X'
                    current_pos += 1
                elif move is None:  # Not chosen yet
                    # Just skip this without doing anything
                    text[current_pos] = ' '
                    current_pos += 1

        print(' ' + text[0] + ' │ ' + text[1] + ' │ ' + text[2])
        print(' ──┼───┼──')
        print(' ' + text[3] + ' │ ' + text[4] + ' │ ' + text[5])
        print(' ──┼───┼──')
        print(' ' + text[6] + ' │ ' + text[7] + ' │ ' + text[8])

    def check_for_win(self):
        # Vars
        found_null = False  # If check for win will not find a win and will not found a null (empty move) then it's draw
        output = [False, None]
        winning_rows = [
            self.line1,  # Horizontal in line 1
            self.line2,  # Horizontal in line 2
            self.line3,  # Horizontal in line 3
            [self.line1[0], self.line2[0], self.line3[0]],  # Vertical 1
            [self.line1[1], self.line2[1], self.line3[1]],  # Vertical 2
            [self.line1[2], self.line2[2], self.line3[2]],  # Vertical 3
            [self.line1[0], self.line2[1], self.line3[2]],  # Diagonal 1
            [self.line3[0], self.line2[1], self.line1[2]]  # Diagonal 2
        ]
        for row in winning_rows:
            # Vars
            win = True
            starting_move = None  # The first move found in the row

            for move in row:
                if win:
                    if move is None:
                        found_null = True
                        win = False  # If there is an unplayed move in the row it can't be a win
                    elif type(move) is bool:  # If is a played move
                        if starting_move is None:  # If is the first move found in rhe winning_row
                            starting_move = move
                        elif starting_move != move:  # If has been found an opponent's move in the winning row
                            win = False

            if win:  # If a winner has been found
                winner = starting_move
                output = [True, winner]
                break

            elif not win:
                if found_null:  # If there is still moves to play
                    output = [False, None]
                else:  # If draw
                    output = [True, None]

        return output
        # Output format
        # [Ending, winner]
        # Ending is true if the play has finished.
        # Winner is true if winner is O, is false if winner is X
        # If ending is true and winner is None, it's a draw.


if __name__ == '__main__':
    current_play = TicTacToe()
    current_play.display_grid()
    playing = True
    player = True
    next_player = None
    print()
    while playing:
        if player:
            player_string = 'O'
            next_player = False
        else:
            player_string = 'X'
            next_player = True
        move_to_save = int(input("Play "+player_string+"'s turn: "))
        save_status = current_play.save_a_move(player, move_to_save)
        while save_status == 0:
            move_to_save = int(input("Sorry, this move is already taken, please choose another move: "))
            save_status = current_play.save_a_move(player, move_to_save)
        if save_status == 1:
            current_play.display_grid()
            is_winning = current_play.check_for_win()
            if is_winning[0]:
                playing = False
                if is_winning[1] is None:
                    print("Its a draw")
                else:
                    if not is_winning[1]:  # If false is winning
                        winner = 'X'
                    else:
                        winner = 'O'
                    print(str(winner)+' won')
                break
            else:
                player = next_player
                continue
