import random
class Rpc_game():
    def __init__(self):
        self.player = True
        self.player_input = 'nothing'

    #Get user input (DONE)
    def get_user_input(self):
        # 1 ask/prompt user for input
        # store user input
        user_input = input('Enter rock, paper or scissor')

        # change player input to user input
        self.player_input = user_input.strip().lower()

    #Get computer random input
    def generate_computer_input(self):
      options = ['rock', 'paper', 'scissor']
      #Generate/select randomly from 3 options
      #change self.cmoputer.input to equate to the random choice
      rand_int = random.randint(0,2)
      #print(rand_int)
      #print(options[rand_int])
      self.computer_input = options[rand_int]
      #print('Computer input:', self.computer_input)

    #Compare results
    def game_result(self):
        if self.player_input == self.computer_input:
            return 'draw'
        elif self.player_input == 'rock' and self.computer_input == 'paper':
            return 'You lose'
        elif self.player_input == 'paper' and self.computer_input == 'rock':
            return 'You win'
        elif self.player_input == 'scissor' and self.computer_input == 'paper':
            return 'You win'
        elif self.player_input == 'paper' and self.computer_input == 'scissor':
            return 'You lose'
        elif self.player_input == 'scissor' and self.computer_input == 'rock':
            return 'You lose'
        elif self.player_input == 'rock' and self.computer_input == 'scissor':
            return 'You win!'
        else:
            return 'Please type rock paper or scissors'
    def run_game(self):
        while True:
            self.get_user_input()
            self.generate_computer_input()
            print(self.game_result())
            player_option_input = input('Play again? y/n')
            if player_option_input == 'n':
                break

game = Rpc_game()
#game.get_user_input()
#print(game.player_input)
game.run_game()

game.generate_computer_input()

#
# game_ran = Rpc_game()
# game_ran.geme_result()
# print(game_ran)
#
# game_ran.generate_computer_input()

