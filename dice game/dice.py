import random
def dice():
    return random.randint(1,6)
def dice_player():
    print('dice game :player 1 vs player2')
    player1 = dice()
    player2 = dice()

    print(f'Player 1 rolled: {player1}')
    print(f'Player 2 rolled: {player2}')
    if player1 > player2:
        print('player 1 wins')
    elif player1 < player2 :
        print('player 2 wins')
    else:
        print('draw')

dice_player()

