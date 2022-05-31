class GuessingGame():
    def __init__(self, answer):
        self.answer = answer

    def guess(self, user_guess):
        self.user_guess = user_guess
        if user_guess < self.answer :
            return 'low'
        elif user_guess > self.answer :
            return 'high'
        else:
            return "correct"
    
    def solved(self):
        return self.user_guess == self.answer

game = GuessingGame(10)
print(game.guess(10))
print(game.solved())
