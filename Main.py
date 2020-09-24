import os

from model.Deck import Deck
from model.Player import Player

# nr_of_players = input("Number of players: ")
from view.Display import ScreenBuilder


header = """
  _____                                          _____
 |A .  | _____                                  |A .  | _____
 | /.\ ||A ^  | _____                           | /.\ ||A ^  | _____
 |(_._)|| / \ ||A _  | _____     BLACKJACK      |(_._)|| / \ ||A _  | _____
 |  |  || \ / || ( ) ||A_ _ |                   |  |  || \ / || ( ) ||A_ _ |
 |____V||  .  ||(_'_)||( v )|      NIGHT        |____V||  .  ||(_'_)||( v )|
        |____V||  .  |      |                          |____V||  .  ||     |
               |____V||  .  |                                 |____V||  .  |
                      |____V|                                        |____V|
"""

def header_with_message(msg):
    return """
      _____                              
     |A .  | _____                  
     | /.\ ||A ^  | _____            
     |(_._)|| / \ ||A _  | _____     
     |  |  || \ / || ( ) ||A_ _ |    
     |____V||  .  ||(_'_)||( v )|     {{message}}
            |____V||  .  |      |     
                   |____V||  .  |      
                          |____V|     
    """.replace("{{message}}", msg)

sb = ScreenBuilder()
sb.with_header(header)
sb.with_question("    New Game (Y/n): ")
new_game = sb.build_and_get_input()

if not new_game:
    exit()



sb.with_question("    Nr Of Players: ")
nr_of_players = sb.build_and_get_input()

deck = Deck()

dealer = Player("Dealer")
player1 = Player("player1")

dealer.add_card_to_hand(deck.draw_card())

player1.add_card_to_hand(deck.draw_card())
player1.add_card_to_hand(deck.draw_card())


sb.with_header(header_with_message(player1.name + "'s  turn!"))

content = player1.get_hand_display() + "\n\n\n\t\t\t\tpress (D) to Draw another card\n\t\t\t\tpress (E) to End your turn\n"
sb.with_question(content)
does_continue = sb.build_and_get_input()

while does_continue:
    player1.add_card_to_hand(deck.draw_card())
    content = player1.get_hand_display() + "\n\n\n\t\t\t\tpress (D) to Draw another card\n\t\t\t\tpress (E) to End your turn\n"
    sb.with_question(content)
    does_continue = sb.build_and_get_input()

