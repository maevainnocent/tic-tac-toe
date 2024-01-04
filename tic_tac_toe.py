def print_table(table):
    for row in table:
        print(" | ".join(row))
        print("-" * 9)

def check_win(table, player):
    for i in range(3):
        if all([cell == player for cell in table[i]]) or \
           all([table[j][i] == player for j in range(3)]):
            return True
    return table[0][0] == table[1][1] == table[2][2] == player or \
           table[0][2] == table[1][1] == table[2][0] == player

def check_draw(table):
    return all(all(cell != " " for cell in row) for row in table)

def appropriate_move(move, table):
    if move.isdigit():
        move = int(move) - 1
        if move >= 0 and move < 9:
            row, col = divmod(move, 3)
            if table[row][col] == " ":
                return True, row, col
    return False, None, None

def tic_tac_toe():
    table = [[" " for _ in range(3)] for _ in range(3)]
    player_1, player_2 = "X", "O"

    while True:
        print_table(table)
        move = input(f"Player {player_1}, enter your move (1-9): ")
        appropriate, row, col = appropriate_move(move, table)

        if not appropriate:
            print("Inappropriate move. Please try again.")
            continue

        table[row][col] = player_1
        if check_win(table, player_1):
            print_table(table)
            print(f"Player {player_1} wins!")
            break
        if check_draw(table):
            print_table(table)
            print("It's a draw!")
            break

        player_1, player_2 = player_2, player_1

if __name__ == "__main__":
    tic_tac_toe()
