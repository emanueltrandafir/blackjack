from model.Card import Card


class BlackjackCard(Card):
    def get_values(self):
        if self.value <= 10:
            return [self.value]
        elif self.value == 11:
            return [1, 11]
        else:
            return [10]