# =========================================
# TIC TAC TOE - HUMAN vs AI (MINIMAX)
# =========================================

def display(b):
    print(f" {b[0]} | {b[1]} | {b[2]} ")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]} ")
    print()


def winner(b, sym):
    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for x,y,z in combos:
        if b[x] == b[y] == b[z] == sym:
            return True
    return False


def full(b):
    for cell in b:
        if cell == " ":
            return False
    return True


def choose():
    while True:
        s = input("Choose X or O: ").upper()
        if s in ["X", "O"]:
            return s
        print("Invalid choice.")


def player_turn(b, p):
    while True:
        try:
            pos = int(input("Enter position (0-8): "))
            if 0 <= pos <= 8 and b[pos] == " ":
                b[pos] = p
                return
            print("Invalid move.")
        except:
            print("Enter a number only.")


def minimax_algo(b, turn, ai, human):

    if winner(b, ai):
        return 1
    if winner(b, human):
        return -1
    if full(b):
        return 0

    if turn:   # AI turn
        best = -10
        for i in range(9):
            if b[i] == " ":
                b[i] = ai
                score = minimax_algo(b, False, ai, human)
                b[i] = " "
                best = max(best, score)
        return best
    else:      # Human turn
        best = 10
        for i in range(9):
            if b[i] == " ":
                b[i] = human
                score = minimax_algo(b, True, ai, human)
                b[i] = " "
                best = min(best, score)
        return best


def ai_turn(b, ai, human):
    best_score = -10
    move = 0

    for i in range(9):
        if b[i] == " ":
            b[i] = ai
            score = minimax_algo(b, False, ai, human)
            b[i] = " "
            if score > best_score:
                best_score = score
                move = i

    b[move] = ai


def game():
    board = [" "] * 9

    human = choose()
    ai = "O" if human == "X" else "X"

    print("\nBoard positions:")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8\n")

    while True:
        display(board)
        player_turn(board, human)

        if winner(board, human):
            display(board)
            print("🎉 You win!")
            break
        if full(board):
            display(board)
            print("🤝 Draw!")
            break

        ai_turn(board, ai, human)

        if winner(board, ai):
            display(board)
            print("🤖 AI wins!")
            break


# --------- Start Game ----------
game()