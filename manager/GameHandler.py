import time
from model.blackjack.BlackjackDeck import BlackjackDeck
from model.blackjack.BlackjackPlayer import BlackjackPlayer


class GameHandler:
    WAIT_BETWEEN_TURNS = .2  # 200 millis

    def __init__(self, players, screen_builder):
        self.deck = BlackjackDeck()
        self.screen_builder = screen_builder
        self.players = []
        self.dealer = BlackjackPlayer("Igor (Dealer)", 99, "RUS", 99999)
        self.players = players



    def play_game(self):
        self.setup_game()
        self.start_game()
        self.finish_game()

    def setup_game(self):
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

                if player.still_playing():
                    player.stands = not self.ask_if_continue()

                    if not player.stands:
                        self.player_draws_card(player)

                player.is_his_turn = False
        self.dealer_draws_cards()

    def finish_game(self):
        winner = self.dealer
        for p in self.players:
            if p.calculate_best_score() > winner.calculate_best_score():
                winner = p
        self.screen_builder.with_header("Game ended: {0} won!".format(winner.name))
        self.screen_builder.with_body(self.get_game_state_display())
        self.screen_builder.with_question("\n\t {0} won. \n\n\t Press any key to continue..".format(winner.name)).build_and_get_input()

    def player_draws_card(self, player):
        player.add_card_to_hand(self.deck.draw_card())

    def dealer_draws_cards(self):
        while not self.dealer.exceeded_dealer_drawing_score():
            time.sleep(GameHandler.WAIT_BETWEEN_TURNS * 3)
            self.player_draws_card(self.dealer)
            self.screen_builder.with_body(self.get_game_state_display()).build()

    def ask_if_continue(self):
        self.screen_builder.with_body(self.get_game_state_display())
        question = "\n\n\n\t\t\t\tHIT!\tpress (H) to Draw another card\n\n\t\t\t\tSTAND!\tpress (S) to End your turn\n >> "
        self.screen_builder.with_question(question)
        response = ""
        while response not in ["h", "s"]:
            response = self.screen_builder.build_and_get_input().lower()
        return response == "h"

    def get_game_state_display(self):
        content = "  " + self.dealer.get_player_infos_str()
        for player in self.players:
            content += player.get_player_infos_str()
        return content

    def wait_and_rerender_hands(self):
        time.sleep(GameHandler.WAIT_BETWEEN_TURNS)
        self.screen_builder.with_body(self.get_game_state_display()).build()

    def is_not_finished(self):
        for player in self.players:
            if player.still_playing():
                return True
        return False
