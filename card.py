class Card:
    def __init__(self, card_id, word, agent):
        self.card_id = card_id
        self.word = word
        self.agent = agent
        self.visible = False

    def Unfold(self):
        self.visible = True