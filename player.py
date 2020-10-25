
class Player():

    def __init__(self, id):
        self.card1 = None
        self.card2 = None
        self.card_to_play = None
        self.player_id = id
        self.protected = False
        self.knowledge_opponent = None

    def draw(self, card):
        if self.card1 is None:
            self.card1 = card
        else:
            self.card2 = card

    def resolve(self):
        player_lost = 0
        action = None
        self.protected = False
        if self.card_to_play == 1:
            card = self.card1
        else:
            card = self.card2

        print(card)
        if card == 1:
            pass
        if card == 2:
            action = 'Reveal'
        if card == 3:
            action = 'Compare'
        if card == 4:
            self.protected = True
        if card == 5:
            pass
        if card == 6:
            action = 'Exchange'
        if card == 7:
            pass
        if card == 8:
            player_lost = self.player_id

        if self.card_to_play == 1:
            self.card1 = self.card2
            self.card2 = None
        else:
            self.card2 = None

        return card, player_lost, action


    def choose_card_to_play(self):
        return 1


    def play(self):
        self.card_to_play = self.choose_card_to_play()
        card, player_lost, action = self.resolve()
        self.card2 = None

        return card, player_lost, action


    def display_hand(self):
        print(self.card1, self.card2)
