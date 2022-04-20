import numpy as np


def play_game():
      player_one_turn()
      play_on = check_player_one_win()
      if play_on == True:
        player_two_turn()
        play_on = check_player_two_win()
      return play_on


def player_one_turn():
      global board
      choice = input('Choose a spot on the board to mark with an X in the format: 0,0')
      choice = choice.split(",")
      spot_one = (int(choice[0]))
      spot_two = (int(choice[1]))

      spots = check_if_valid(spot_one, spot_two)
      spot_one = spots[0]
      spot_two = spots[1]

      spots = check_if_taken(spot_one, spot_two)
      spot_one = spots[0]
      spot_two = spots[1]

      board_spots[spot_one, spot_two] = 'X'
      board = (f"{board_spots[0, 0]}  |  {board_spots[0, 1]}  |  {board_spots[0, 2]}\n"
               "______________\n"
               f"{board_spots[1, 0]}  |  {board_spots[1, 1]}  |  {board_spots[1, 2]}\n"
               "______________\n"
               f"{board_spots[2, 0]}  |  {board_spots[2, 1]}  |  {board_spots[2, 2]}\n")
      print(board)


def player_two_turn():
      global board
      choice = input('Choose a spot on the board to mark with an O in the format: 0,0')
      choice = choice.split(",")
      spot_one = (int(choice[0]))
      spot_two = (int(choice[1]))

      spots = check_if_valid(spot_one, spot_two)
      spot_one = spots[0]
      spot_two = spots[1]

      spots = check_if_taken(spot_one, spot_two)
      spot_one = spots[0]
      spot_two = spots[1]

      board_spots[spot_one, spot_two] = 'O'
      board = (f"{board_spots[0, 0]}  |  {board_spots[0, 1]}  |  {board_spots[0, 2]}\n"
               "______________\n"
               f"{board_spots[1, 0]}  |  {board_spots[1, 1]}  |  {board_spots[1, 2]}\n"
               "______________\n"
               f"{board_spots[2, 0]}  |  {board_spots[2, 1]}  |  {board_spots[2, 2]}\n")
      print(board)


def check_player_one_win():
      if (board_spots[0, 0] == 'X' and board_spots[0, 1] == 'X' and board_spots[0, 2] == 'X'):
          print('Player 1 Wins!')
          return False
      elif (board_spots[1, 0] == 'X' and board_spots[1, 1] == 'X' and board_spots[1, 2] == 'X'):
          print('Player 1 Wins!')
          return False
      elif (board_spots[2, 0] == 'X' and board_spots[2, 1] == 'X' and board_spots[2, 2] == 'X'):
          print('Player 1 Wins!')
          return False
      elif (board_spots[0, 0] == 'X' and board_spots[0, 1] == 'X' and board_spots[0, 2] == 'X'):
          print('Player 1 Wins!')
          return False
      elif (board_spots[0, 1] == 'X' and board_spots[1, 1] == 'X' and board_spots[2, 1] == 'X'):
          print('Player 1 Wins!')
          return False
      elif (board_spots[0, 2] == 'X' and board_spots[1, 2] == 'X' and board_spots[2, 2] == 'X'):
          print('Player 1 Wins!')
          return False
      elif (board_spots[0, 0] == 'X' and board_spots[1, 1] == 'X' and board_spots[2, 2] == 'X'):
          print('Player 1 Wins!')
          return False
      elif (board_spots[2, 0] == 'X' and board_spots[1, 1] == 'X' and board_spots[0, 2] == 'X'):
          print('Player 1 Wins!')
          return False
      else:
          return True


def check_player_two_win():
    if (board_spots[0, 0] == 'O' and board_spots[0, 1] == 'O' and board_spots[0, 2] == 'O'):
        print('Player 1 Wins!')
        return False
    elif (board_spots[1, 0] == 'O' and board_spots[1, 1] == 'O' and board_spots[1, 2] == 'O'):
        print('Player 1 Wins!')
        return False
    elif (board_spots[2, 0] == 'O' and board_spots[2, 1] == 'O' and board_spots[2, 2] == 'O'):
        print('Player 1 Wins!')
        return False
    elif (board_spots[0, 0] == 'O' and board_spots[0, 1] == 'O' and board_spots[0, 2] == 'O'):
        print('Player 1 Wins!')
        return False
    elif (board_spots[0, 1] == 'O' and board_spots[1, 1] == 'O' and board_spots[2, 1] == 'O'):
        print('Player 1 Wins!')
        return False
    elif (board_spots[0, 2] == 'O' and board_spots[1, 2] == 'O' and board_spots[2, 2] == 'O'):
        print('Player 1 Wins!')
        return False
    elif (board_spots[0, 0] == 'O' and board_spots[1, 1] == 'O' and board_spots[2, 2] == 'O'):
        print('Player 1 Wins!')
        return False
    elif (board_spots[2, 0] == 'O' and board_spots[1, 1] == 'O' and board_spots[0, 2] == 'O'):
        print('Player 1 Wins!')
        return False
    else:
        return True


def check_if_taken(spot_one, spot_two):
    valid_choice = True
    while valid_choice:
        if board_spots[spot_one, spot_two] == 'X' or board_spots[spot_one, spot_two] == 'O':
            choice = input('Please choose a spot that hasn\'t already been taken.')
            choice = choice.split(",")
            spot_one = (int(choice[0]))
            spot_two = (int(choice[1]))
            spots = [spot_one, spot_two]
        else:
            spots = [spot_one, spot_two]
            valid_choice = False
    return spots


def check_if_valid(spot_one, spot_two):
    valid_choice = True
    while valid_choice:
        if  (spot_one < 0 or spot_one > 2) or (spot_two < 0 or spot_two > 2):
            choice = input('Please enter a valid position on the board')
            choice = choice.split(",")
            spot_one = (int(choice[0]))
            spot_two = (int(choice[1]))
            spots = [spot_one, spot_two]
        else:
            spots = [spot_one, spot_two]
            valid_choice = False
    return spots


board_spots = [' ' for spot in range(9)]
board_spots = np.array(board_spots)
board_spots = board_spots.reshape(3, 3)

board = (f"{board_spots[0, 0]}  |  {board_spots[0, 1]}  |  {board_spots[0, 2]}\n"
      "______________\n"
      f"{board_spots[1, 0]}  |  {board_spots[1, 1]}  |  {board_spots[1, 2]}\n"
      "______________\n"
      f"{board_spots[2, 0]}  |  {board_spots[2, 1]}  |  {board_spots[2, 2]}\n")

print('Player 1 will be marking their spots with an \'X\'')
print('Player 2 will be marking their spots with an \'O\'')
print('Location 0,0 denotes the position at row 0, column 0.')
print(board)

play_on = True
while play_on:
      play_on = play_game()
      another_game = None
      if play_on == False:
          another_game = input('That was fun! Would you like to play again? Type \'y\' if so, and anything else to stop playing')
      if another_game == 'y':
          play_on = True
          board_spots = [' ' for spot in range(9)]
          board_spots = np.array(board_spots)
          board_spots = board_spots.reshape(3, 3)

          board = (f"{board_spots[0, 0]}  |  {board_spots[0, 1]}  |  {board_spots[0, 2]}\n"
                   "______________\n"
                   f"{board_spots[1, 0]}  |  {board_spots[1, 1]}  |  {board_spots[1, 2]}\n"
                   "______________\n"
                   f"{board_spots[2, 0]}  |  {board_spots[2, 1]}  |  {board_spots[2, 2]}\n")





