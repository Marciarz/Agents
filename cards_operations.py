from card import Card
import random
import main

def Read_file_with_words(number_of_cards):
    words_list = []
    chosen_words_list = []
    with open("dictionary.txt") as file:
        for line in file:
            if "ść" not in line and len(line) < 14:
                words_list.append(line)

    all_words_count = len(words_list)
    while len(chosen_words_list) != number_of_cards:
        index = random.randint(0, all_words_count)
        chosen_word = words_list[index]
        if chosen_word not in chosen_words_list:
            chosen_words_list.append(chosen_word.rstrip('\n'))

    return chosen_words_list


def Add_cards(cards_quantity, agent_value, cards_dictionary, available_numbers, words_list):
    card_number = 1
    while card_number <= cards_quantity:
        used_numbers = list(cards_dictionary.keys())
        id = random.randint(1, available_numbers)

        while id in used_numbers:
            id = random.randint(1, available_numbers)

        already_existing_words = []
        for card in cards_dictionary:
            already_existing_words.append(cards_dictionary[card].word)

        duplicated_word = True
        while duplicated_word:
            chosen_word = words_list[random.randint(0, available_numbers - 1)]
            if chosen_word not in already_existing_words:
                duplicated_word = False

        cards_dictionary[id] = Card(id, chosen_word, agent_value)
        card_number += 1

    return cards_dictionary

def Create_all_cards(cards_to_be_created, number_of_cards):
    all_cards = {}
    words_list = Read_file_with_words(number_of_cards)
    for row in cards_to_be_created:
        all_cards = Add_cards(row[0], row[1], all_cards, number_of_cards, words_list)
    return all_cards

def Generating_cards(number_of_cards):
    cards_to_be_created = ((5, "red"), (5, "blue"), (1, "black"), (14, "brown"))
    all_cards = Create_all_cards(cards_to_be_created, number_of_cards)
    return all_cards