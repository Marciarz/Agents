from card import Card
import random

def Add_cards(cards_quantity, agent_value, cards_dictionary, available_numbers):
    card_number = 1
    while card_number <= cards_quantity:
        used_numbers = list(cards_dictionary.keys())
        id = random.randint(1, available_numbers)

        while id in used_numbers:
            id = random.randint(1, available_numbers)

        cards_dictionary[id] = Card(id, "card-{}".format(id), agent_value)
        card_number += 1

    return cards_dictionary

def Create_all_cards(cards_to_be_created, number_of_cards):
    all_cards = {}
    for row in cards_to_be_created:
        all_cards = Add_cards(row[0], row[1], all_cards, number_of_cards)
    return all_cards

def main(number_of_cards):
    cards_to_be_created = ((5, "red"), (5, "blue"), (1, "black"), (14, "brown"))
    all_cards = Create_all_cards(cards_to_be_created, number_of_cards)
    return all_cards



if __name__ == "__main__":
    number_of_cards = 25
    main(number_of_cards)
