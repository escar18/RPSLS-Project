from player import Player

class HumanPlayer(Player):
    def choose_gesture(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        valid_input = False

        while not valid_input:
            user_input = input(f"{self.name}, please choose a gesture (0-4): ")
            if user_input.isdigit() and int(user_input) in range(5):
                valid_input = True
            else:
                print("Invalid input. Please try again.")

        return gesture_list[int(user_input)]