import random

class Game:
    def __init__(self):
        self.score = 0
        self.guesses = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.library = ['APPLE', 'WOMBAT', 'METICULOUS', 'WALTZ', 'PYTHON']
        self.word = self.library[random.randint(0, len(self.library) - 1)]
        self.guess = list('_' * len(self.word))

    def game_step(self):
        if self.score == 6:
            print("Sorry, you lost")
            return False
        if '_' not in self.guess:
            print("Congratulations, you won")
            return False
        self._draw()
        self._ask_guess()
        self._draw()
        return True

    def _draw(self):
        print("Letters left: " + self.guesses)
        self._draw_body()
        # print("Word = " + self.word)
        print("Guess = " + "".join(self.guess))

    def _ask_guess(self):
        guess = input("Guess a letter ... ")

        while guess not in self.guesses:
            guess = input("Guess again ...")

        # print("guess = " + guess)
        self.guesses = self.guesses.replace(guess, '_', 1)
        if (guess in self.word):
            idx = self._find(guess)
            for i in idx:
                self.guess[i] = guess

    def _remove_guess(self, guess):
        self.guess.replace(guess, '_')

    def _draw_body(self):
        if self.score == 0:
            print(""" 
                      -------
                      |      |
                      |
                      |
                      |
                      |
                      |
                      |
                    -----
                """)
        elif self.score == 1:
            print(""" 
                      -------
                      |      |
                      |      O
                      |
                      |
                      |
                      |
                      |
                    -----
                """)
        elif self.score == 2:
            print(""" 
                      -------
                      |      |
                      |      O
                      |      |
                      |      |
                      |
                      |
                      |
                    -----
                """)
        elif self.score == 3:
            print(""" 
                      -------
                      |      |
                      |      O
                      |      |/
                      |      |
                      |
                      |
                      |
                    -----
                """)
        elif self.score == 4:
            print(""" 
                      -------
                      |      |
                      |      O
                      |     \|/
                      |      |
                      |
                      |
                      |
                    -----
                """)
        elif self.score == 5:
            print(""" 
                      -------
                      |      |
                      |      O
                      |     \|/
                      |      |
                      |       \\
                      |
                      |
                    -----
                """)
        elif self.score == 6:
            print(""" 
                      -------
                      |      |
                      |      O
                      |     \|/
                      |      |
                      |     / \\
                      |
                      |
                    -----
                """)

    def _find(self, guess):
        return [i for i, ltr in enumerate(self.word) if ltr == guess]

if __name__ == '__main__':
    game = Game()
    cont = game.game_step()
    while cont:
        cont = game.game_step()


