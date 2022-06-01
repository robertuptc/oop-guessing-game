class GuessingGame:
    def __init__(self, answer):
        self.answer = answer
        self.check = False

    def guess(self, user_guess):
        if user_guess > self.answer:
            print('high')
        elif user_guess < self.answer:
            print("low")
        else:
            user_guess == self.answer
            self.check = True
            print("correct")

    def solved(self):
        return self.check

x = GuessingGame(25)
(x.guess(26))
print(x.solved())
