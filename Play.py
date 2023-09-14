import random

class Game_Figure:
    def __init__(self):
        self.ran = random.randint(1, 5)
        self.choices = {
            1: 'Rock',
            2: 'Paper',
            3: 'Scissors',
            4: 'Lizard',
            5: 'Spock'
        }
        self.io_choice = self.choices[self.ran]

class Player(Game_Figure):
    def __init__(self):
        super().__init__()
        print('Choice your figure:\n1.Rock\n2.Paper\n3.Scissors\n4.Lizard\n5.Spock')
        self.user_input = int(input('Print number: '))
        if self.user_input in self.choices:
            self.user_choice = self.choices[self.user_input]
        else:
            self.user_choice = None

    def fight(self):
        outcomes = {
            ('Rock', 'Scissors'): 'You win!',
            ('Rock', 'Lizard'): 'You win!',
            ('Paper', 'Rock'): 'You win!',
            ('Paper', 'Spock'): 'You win!',
            ('Scissors', 'Paper'): 'You win!',
            ('Scissors', 'Lizard'): 'You win!',
            ('Lizard', 'Spock'): 'You win!',
            ('Lizard', 'Paper'): 'You win!',
            ('Spock', 'Rock'): 'You win!',
            ('Spock', 'Scissors'): 'You win!'
        }
        if self.user_choice == self.io_choice:
            return 'Draw'
        if self.user_choice is None:
            return 'Invalid'

        if (self.user_choice, self.io_choice) in outcomes:
            return outcomes[(self.user_choice, self.io_choice)]
        else:
            return f"You lose! {self.io_choice} beats {self.user_choice}."

play = Player()
result = play.fight()
print(result)