class Hand:
    def __init__(self):
        super().__init__()
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def display(self):
        res = ""
        for card in self.cards:
            res = res + " |" + card.display() + "|  "
        return res

    def calculate_values(self):
        total_values = [0]
        for card in self.cards:
            card_vals = card.get_values()
            new_total_values = []
            for total_val in total_values:
                for card_val in card_vals:
                    new_total_values.append(total_val + card_val)
            total_values = new_total_values
        return total_values

    def exceeded_value(self, value):
        for val in self.calculate_values():
            if val <= value:
                return
        return True
