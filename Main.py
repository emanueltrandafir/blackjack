import math

from model.blackjack.BlackjackPlayer import BlackjackPlayer
from manager.GameHandler import GameHandler
from view.Display import ScreenBuilder

MAX_NR_OF_PLAYERS = 4
PLAYERS_FILE_NAME = "players.txt"


def main():
    sb = ScreenBuilder()

    while will_play_again(sb):
        sb.with_body("").with_question("\tNew Game (Y/n): Y\n\n\tNumber Of Players (max 4): ")
        nr_of_players = -1
        while int(nr_of_players) < 1 or int(nr_of_players) > 4:
            try:
                nr_of_players = int(sb.build_and_get_input())
            except:
                nr_of_players = -1

        players = read_players_from_file(nr_of_players)

        game = GameHandler(players, sb)
        game.play_game()


def will_play_again(sb):
    sb.with_header("Blackjack Night!").with_body("").with_question("\tNew Game (Y/n): ")
    return sb.build_and_get_input().lower() != "n"


def read_players_from_file(nr_of_players):
    players = []
    with open(PLAYERS_FILE_NAME, 'r') as reader:
        for line in reader:
            if len(players) == nr_of_players:
                return players
            [name, surname, age, country, money] = line.replace("\n", "").split("\t")
            players.append(BlackjackPlayer(name + " " + surname, age, country, money))
    return players


def isInt(num):
    try:
        int(num)
        return True
    except:
        return False


if __name__ == "__main__":
    main()
