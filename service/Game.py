import time

from model.Deck import Deck
from model.Player import Player


class Game:
    WAIT_TIME = .2  # 200 millis

    def __init__(self, nr_of_players, screen_builder):
        self.deck = Deck()
        self.screen_builder = screen_builder
        self.players = []
        self.dealer = Player("Dealer")
        for i in range(0, int(nr_of_players)):
            new_player = Player("Player " + str(i + 1))
            self.players.append(new_player)
        self.init_players_hands()

    def player_draws_card(self, player):
        player.add_card_to_hand(self.deck.draw_card())

    def init_players_hands(self):
        self.screen_builder.with_header("handing out cards..")
        self.wait_and_rerender_hands()
        self.player_draws_card(self.dealer)
        self.wait_and_rerender_hands()
        for player in self.players:
            self.player_draws_card(player)
            self.wait_and_rerender_hands()
            self.player_draws_card(player)
            self.wait_and_rerender_hands()

    def start_game(self):
        while self.is_not_finished():
            for player in self.players:
                self.screen_builder.with_header(player.name + "'s  turn!")
                player.is_his_turn = True
                if not player.stands:
                    player.stands = not self.ask_player_if_continue(player)
                    if not player.stands:
                        self.player_draws_card(player)
                player.is_his_turn = False
            self.wait_and_rerender_hands()

    def ask_player_if_continue(self, player):
        self.screen_builder.with_body(self.get_player_hands_display())
        question = "\n\n\n\t\t\t\tHIT!\tpress (H) to Draw another card\n\n\t\t\t\tSTAND!\tpress (S) to End your turn\n"
        self.screen_builder.with_question(question)
        response = ""
        while response not in ["h", "s"]:
            response = self.screen_builder.build_and_get_input().lower()
        return response == "h"

    def get_player_hands_display(self):
        content = "\t    Dealer      - \t" + self.dealer.get_hand_display()
        for player in self.players:
            content += "\n\n\t"
            content += " -> " if bool(player.is_his_turn) else "    "
            content += player.name
            content += " (s)" if player.stands else "    "
            content += "-\t" + player.get_hand_display()
        return content

    def wait_and_rerender_hands(self):
        time.sleep(Game.WAIT_TIME)
        self.screen_builder.with_body(self.get_player_hands_display()).build()

    def is_not_finished(self):
        for player in self.players:
            if not player.stands:
                return True
        return False
 
