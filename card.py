class Card:
    def __init__(self, card_id, word, agent, is_reset = False):
        self.card_id = card_id
        self.word = word
        self.agent = agent
        self.is_reset = is_reset