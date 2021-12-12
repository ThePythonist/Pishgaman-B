def game():
    board = [1,2,3,4,5,6,7,8,9]
    win_combinations = [
        (0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),
        (2,5,8),(0,4,8),(2,4,6)]
    end = False

    def table():

        print('''
         {} | {} | {}
        -----------
         {} | {} | {}
        -----------
         {} | {} | {}
        '''.format(
            board[0],
            board[1],
            board[2],
            board[3],
            board[4],
            board[5],
            board[6],
            board[7],
            board[8]
        ))

    def choice1():
        while True :
            a = input("Player 1 choose : ")
            try :
                a = int(a)
                a -= 1
                if a in range(9):
                    return a
                else :
                    print("Thats not on the board")
            except ValueError:
                print("Thats not a valid number! Try again")

    def choice2():
        while True:
            a = input("Player 2 choose : ")
            try:
                a = int(a)
                a -= 1
                if a in range(9):
                    return a
                else:
                    print("Thats not on the board")
            except ValueError:
                print("Thats not a valid number! Try again")

    def player1_move():
        n = choice1()
        if board[n] == "X" or board[n] == "O":
            print("You cant choose that")
            player1_move()
        else :
            board[n] = "X"

    def player2_move():
        n = choice2()
        if board[n] == "X" or board[n] == "O":
            print("You cant choose that")
            player2_move()
        else :
            board[n] = "O"

    def check_board() :
        count = 0
        for i in win_combinations:
            if board[i[0]] == board[i[1]] == board[i[2]] == "X" :
                print("Player 1 Wins")
                return True
            elif board[i[0]] == board[i[1]] == board[i[2]] == "O":
                print("Player 2 Wins")
                return True

        for i in range(9):
            if board[i] == "X" or board[i] == "O" :
                count += 1

            if count == 9 :
                print("Game ends level")
                return True

    while not end :
        table()
        end = check_board()
        if end == True :
            break
        player1_move()
        print()
        table()
        end = check_board()
        if end == True :
            break
        player2_move()
        print()

    if input("Play again ? (y/n)") == "y":
        print()
        game()
    else :
        pass
game()
