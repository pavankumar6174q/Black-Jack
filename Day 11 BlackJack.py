import random
def deal_card():
    """Returns a random card from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #cards deck where 11 is ACE, other 3 10's are king, queen and jack
    card = random.choice(cards) #this selects the random card from the deck
    return card 
def calculate_score(cards):
    """"Calculates cards total and also checks for the Black jack"""
    if sum(cards) == 21 and len(cards) == 2: #we are checking whether sum of 2 cards is equal to 21 if yes turn them into 0
        return 0
    elif 11 in cards and sum(cards)> 21:# as per blackjack rules we need to change the ACE 11 to 1 if we have total greater than 21
        cards.remove(11) #here we are removing the 11 from the selected cards
        cards.append(1) #changing it to 1
    return sum(cards) #this returns the sum
def compare(user_score, computer_score): #just basic if else condition just go through
    """Compares the final total of the cards"""
    if user_score > 21 and computer_score > 21:
        return "you went over you lose"
    elif user_score == computer_score:
        return "It's a Draw 😉"
    elif user_score > 21:
        return "you lose you went over"
    elif user_score == 0:
        return "Yay you've won 🙌"
    elif  computer_score == 0:
        return "You lose🤦‍♂️"
    elif computer_score > 21:
        return "You won computer went over"
    elif user_score > computer_score:
        return "Yay you've won 🙌"
    elif computer_score > user_score:
        return "You lose🤦‍♂️" 
def black_jack():
    """"Restarts the entire game"""
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    print(logo)
    is_game_over = False  #the switch to end the game
    user_cards = []
    computer_cards = []
    for i in range(2): #this selects the 2 random items from cards 
        user_cards.append(deal_card()) #this will get added to the user
        computer_cards.append(deal_card()) #this will get added to the computer
    while not is_game_over: 
        user_score = calculate_score(user_cards) #this calculates the user score using calculate function
        computer_score = calculate_score(computer_cards) #this calculates the computer score using calculate function
        print(f'your cards are {user_cards}, your total is {user_score}')
        print(f'computers first card is {computer_cards[0]}') #prints only one card of the computer

        if user_score == 0 or user_score >21 or computer_score == 0 or computer_score > 21:
            is_game_over = True
        else:
            new_card = input("enter y for continue playing and n to stop:  ").lower() #if user wants to pick another card
            if new_card == 'y':
                user_cards.append(deal_card())
                calculate_score(user_cards)
            else:
                is_game_over = True
    while computer_score != 0 and computer_score <17: #after user choice computer needs to pick cards until this satisfies
        computer_cards.append(deal_card())
        computer_score= calculate_score(computer_cards)
    print(f"your cards {user_cards}, your total is {user_score}")
    print(f"computer cars {computer_cards}, computer total is {computer_score}")
    print(compare(user_score, computer_score))

while input("Press 'y' if you want to restart ") == 'y':
    black_jack()
