# from game import Game
# if __name__ == '__main__':
#     game = Game()
#     game.run_game()

from game import Game
from human import HumanPlayer
from ai import AI

def main():
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    print("Game Rules:")
    print("If Rock crushes Scissors then Rock wins")
    print("If Scissors cuts Paper then Scissors wins")
    print("If Paper covers Rock then Paper wins")
    print("If Rock crushes Lizard then Rock wins")
    print("If Lizard poisons Spock then Lizard wins")
    print("If Spock smashes Scissors then Spock wins")
    print("If Scissors decapitates Lizard then Scissors wins")
    print("If Lizard eats Paper then Lizard wins")
    print("If Paper disproves Spock then Paper wins")
    print("If Spock vaporizes Rock then Spock wins")
    print()

    play_again = True

    while play_again:
        num_human_players = None
        while num_human_players not in [1, 2, 3]:
            try:
                num_human_players = int(input("How many human players will be playing? (1, 2, or 3): "))
            except ValueError:
                print("Invalid input. Please enter a number.")

        players = []
        for i in range(num_human_players):
            player_name = input(f"Enter the name for Human Player {i + 1}: ")
            players.append(HumanPlayer(player_name))

        include_ai = input("Do you want to include an AI player? (y/n): ")
        while include_ai.lower() not in ["y", "n"]:
            print("Invalid input. Please try again.")
            include_ai = input("Do you want to include an AI player? (y/n): ")

        if include_ai.lower() == "y":
            ai_name = input("Enter the name for the AI player: ")
            players.append(AI(ai_name))
        else:
            print("there will be no AI player")

        game = Game()
        for i in range(len(players)):
            for j in range(i + 1, len(players)):
                print(f"Game {i + 1} - {players[i].name} vs {players[j].name}")
                game.play_game(players[i], players[j])
                print()

        play_again_input = input("Do you want to play again? (y/n): ")
        play_again = play_again_input.lower() == "y"

if __name__ == "__main__":
    main()