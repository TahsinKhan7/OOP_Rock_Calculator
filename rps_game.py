import random

class Rock_Paper_Scissor:
    def __init__(self):
        self.rock = True
        self.paper = True
        self.scissor = True
    def player_move(self, player_input):
        self.input = player_input
        #player_input = input('Enter rock, paper or scissor')
        return self.input

    def comp_move(self, comp_ran):
        self.comp_ran = comp_ran

        rps_ran = ['rock', 'paper', 'scissor']
        comp_ran = random.choice(rps_ran)
        return self.comp_ran

    def comp_input(self):

        if self.input == self.comp_ran:
            print('Tie')
        elif self.input == 'rock' and self.comp_ran == 'scissor':
            print('You win!')
        elif self.input == 'paper' and self.comp_ran == 'rock':
            print('You win')
        elif self.input == 'scissor' and self.comp_ran == 'paper':
            print('You win')

        elif self.input == 'scissor' and self.comp_ran == 'rock':
            print('You lose')
        elif self.input == 'rock' and self.comp_ran == 'paper':
            print('You lose')
        elif self.input == 'paper' and self.comp_ran == 'scissor':
            print('You lose')
        else:
            print('please select either rock, paper, or scissor')



play = Rock_Paper_Scissor()
play.player_move('rock')
print('you picked', play.player_move)

#Rock_Paper_Scissor.comp_move(comp_ran=)

# Rock_Paper_Scissor()
#  = Rock_Paper_Scissor()



