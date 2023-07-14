class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def choose_gesture(self):
        pass

    def update_score(self, result):
        if result == "win":
            self.score += 1