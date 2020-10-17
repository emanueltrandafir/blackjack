from model.Player import Player


class BlackjackPlayer(Player):
    DEALER_DRAWING_TRESHOLD = 17
    MAX_HAND_VALUE = 21

    def __init__(self, name, age, country_code, amount):
        super().__init__(name, age, country_code, amount)
        self.stands = False
        self.bid = 0

    def exceeded_dealer_drawing_score(self):
        return self.hand.exceeded_value(BlackjackPlayer.DEALER_DRAWING_TRESHOLD)

    def exceeded_max(self):
        return self.hand.exceeded_value(BlackjackPlayer.MAX_HAND_VALUE)

    def still_playing(self):
        return not self.stands and not self.exceeded_max()

    def calculate_best_score(self):
        vals = super().get_hand_values()
        vals.sort(reverse=True)
        for val in vals:
            if val <= 21:
                return val
        return -1

    def get_status_str(self):
        if self.stands:
            return "(s)"
        if self.exceeded_max():
            return "(e)"
        return "   "

    def get_player_infos_str(self):
        arrow = "->" if bool(self.is_his_turn) else "  "
        bid = "\t" if "dealer" in self.name.lower() else (str(self.bid) + ".00$")
        return "\n\n    {0} [{1}] {2}({5}) {6} {3} -    {4}".format(
            arrow, self.calculate_best_score(), self.name, self.get_status_str(), self.get_hand_display(), self.country_code, bid)