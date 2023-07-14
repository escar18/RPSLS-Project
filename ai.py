

from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def choose_gesture(self):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        chosen_gesture = random.randint(0, 4)
        sleep(1)
        print(f"{self.name} has picked {gesture_list[chosen_gesture]}")
        return gesture_list[chosen_gesture]
