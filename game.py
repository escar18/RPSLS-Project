class Game:
    def __init__(self):
        self.rounds_to_win = 2

    def play_game(self, player1, player2):
        player1.score = 0  # Reset player1's score
        player2.score = 0  # Reset player2's score

        while player1.score < self.rounds_to_win and player2.score < self.rounds_to_win:
            gesture1 = player1.choose_gesture()
            gesture2 = player2.choose_gesture()
            result = self.compare_gestures(gesture1, gesture2)
            self.display_round_result(player1.name, gesture1, player2.name, gesture2, result)
            self.update_scores(player1, player2, result)
            self.display_scores(player1, player2)

        if player1.score > player2.score:
            print(f"{player1.name} wins the game!")
        else:
            print(f"{player2.name} wins the game!")


    @staticmethod
    def compare_gestures(gesture1, gesture2):
        if gesture1 == gesture2:
            return "tie"

        winning_gestures = {
            "Rock": ["Scissors", "Lizard"],
            "Paper": ["Rock", "Spock"],
            "Scissors": ["Paper", "Lizard"],
            "Lizard": ["Paper", "Spock"],
            "Spock": ["Rock", "Scissors"]
        }

        if gesture1 in winning_gestures and gesture2 in winning_gestures[gesture1]:
            return "player1"
        elif gesture2 in winning_gestures and gesture1 in winning_gestures[gesture2]:
            return "player2"
        else:
            return "tie"

    @staticmethod
    def display_round_result(player1_name, gesture1, player2_name, gesture2, result):
        if result == "tie":
            print("It's a tie!")
        elif result == "player1":
            print(f"{player1_name} wins! {gesture1} beats {gesture2}.")
        else:
            print(f"{player2_name} wins! {gesture2} beats {gesture1}.")

    @staticmethod
    def update_scores(player1, player2, result):
        if result == "player1":
            player1.score += 1
        elif result == "player2":
            player2.score += 1

    @staticmethod
    def display_scores(player1, player2):
        print(f"Score: {player1.name}: {player1.score}, {player2.name}: {player2.score}")