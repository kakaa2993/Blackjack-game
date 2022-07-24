#!/usr/bin/python3

from art import logo
import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def player_card_generator():
    player_cards = []
    new_card = random.choice(cards)
    player_cards.append(new_card)
    player_cards.append(new_card)
    return player_cards

def computer_card_generator(first_card):
    computer_cards = [first_card]
    while sum(computer_cards) < 17:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
    return computer_cards

os.system("clear")
the_game_is_running = True
def blackjack():
    want_to_play = input("Do you want to play the 'BLACKJACK' game? type 'y' or 'n': ")
    while want_to_play == "y":
        print(logo)
        player_cards = player_card_generator()
        computer_cards = [random.choice(cards)]
        
        print(player_cards)
        print(computer_cards)

        want_to_play = 'n'

blackjack()
