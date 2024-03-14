import random
def deal_card():
    """returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)
def calculate_score(cards):
    """takes a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        if  11 cards in sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
def compare(user_score, computer_score):
    """compare the final scores between the user and computer."""
    if user_score > 21 and computer_score > 21:
        return "you went over. you lose!"
    if user_score == computer_score:
        return "Its a draw!"
    elif computer_score == 0:
        return "Computer has a blackjack! You lose!"
    elif user_score == 0:
        return "You have a blackjack! You win!"
    elif user_score > 21:
        return: "You went over! You lose!"
    elif computer_score > 21:
        return: "Computer went over! You win!"
    elif user_score > computer_score:
        return: "You win!"
    else:
        return "You Lose!"
def play_game():
    """Play a game of blackjack"""
    user_cards = []
    computer_cards = []
    is_game_over = false
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: [user _cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            else:
                should_continue = input("Type 'y' to get another card, or 'n' to pass:")
                if should_continue == 'y':
                    user_cards.append(deal_card())
                else: is_game_over = True
