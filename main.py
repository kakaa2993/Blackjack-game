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
    if sum(player_cards)> 21:
            if 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)

    return player_cards

def computer_card_generator(first_card):
    computer_cards = [first_card]
    while sum(computer_cards) < 17:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        if sum(computer_cards)> 21:
            if 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
    
    return computer_cards

os.system('clear')
the_game_is_running = True
want_to_play = input("Do you want to play the 'BLACKJACK' game? type 'y' or 'n': ")
def blackjack(): 
    player_cards = player_card_generator()
    computer_first_card = random.choice(cards)
    computer_cards = computer_card_generator(computer_first_card)
    computer_score = sum(computer_cards)
    get_another_card = "y"

    while get_another_card == 'y':
        os.system("clear")
        print(logo)
        player_score = sum(player_cards)
        print(f"   Your cards: {player_cards} , current score: {player_score}")
        print(f"   Computer's first cards: {computer_first_card}")

        if computer_score == 21 or player_score == 21:
            get_another_card == "n"
        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == 'y':
                new_card = random.choice(cards)
                player_cards.append(new_card)
                player_score = sum(player_cards)
                if player_score> 21:
                    if 11 in player_cards:
                        player_cards.remove(11)
                        player_cards.append(1)
                    else:
                        get_another_card = 'n'

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    
    #The result:
    if player_score == 21:
        print("Win with a blackjack 😎")
    elif abs(computer_score - 21 ) < abs(player_score - 21):
        print("You lose 😭")
    elif abs(computer_score - 21 ) == abs(player_score - 21):
        print("It's a Draw")
    else:
        print("You win 😃")

    player_replay = input("Do you want to play the 'BLACKJACK' game? type 'y' or 'n': ")
    if player_replay == "y":
        blackjack()
    
if want_to_play == "y":        
    blackjack()

