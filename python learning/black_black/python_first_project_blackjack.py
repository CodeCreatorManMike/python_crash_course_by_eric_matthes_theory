# import statements
import random
import json

# --- JSON persistence functions ---
def load_player_data():
    try:
        with open("json_black_jack_save_user_information.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data

def save_player_data(data):
    with open("json_black_jack_save_user_information.json", "w") as f:
        json.dump(data, f, indent=4)

# --- title - designed by ChatGPT / calling it before game starts ---
def print_blackjack_logo():
    logo = r"""
 ____  _            _        _            _
| __ )| | __ _  ___| | __   | | __ _ ___ | | __ 
|  _ \| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ / 
| |_) | | (_| | (__|   <    | | (_| | (__|   <  
|____/|_|\__,_|\___|_|\_\   |_|\__,_|\___|_|\_\ 

╔═══════════════════════════════════════════════╗
║           W E L C O M E  T O  T H E           ║
║               B L A C K J A C K               ║
║                   T A B L E                   ║
╚═══════════════════════════════════════════════╝
"""
    print(logo)

print_blackjack_logo()

# --- assign users / login ---
player_data = load_player_data()  # load existing users

username = input("Enter your username: ")

if username not in player_data:
    print(f"Welcome, {username}! Creating new account...")
    player_data[username] = {"chips": 500, "rounds_played": 0, "wins": 0}
else:
    print(f"Welcome back, {username}!")

# project imports 
import random  # make sure this is included at the top

# betting system (this persists across rounds so is outside the round function)
player_chips = player_data[username]["chips"]  # get wallet from JSON

# card definitions
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['♠', '♥', '♦', '♣']

# build deck as tuples
deck_tuples = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck_tuples)

# --- function to display leaderboard ---
def display_leaderboard():
    sorted_players = sorted(player_data.items(), key=lambda x: x[1]["chips"], reverse=True)
    print("\n=== Leaderboard ===")
    for uname, stats in sorted_players:
        print(f"{uname}: Chips={stats['chips']}, Wins={stats['wins']}, Rounds={stats['rounds_played']}")

# --- play a single round of blackjack ---
def play_blackjack_round():
    global player_chips
    global deck_tuples

    # --- game state flags ---
    round_active = True
    player_win = False
    dealer_win = False
    draw = False
    player_second_turn = False

    # stating player chips at the start of each round and first bet deduction
    print(f"\nYou have {player_chips} chips available to bet.")
    bet = 0
    while True:
        try:
            bet = int(input("\nEnter your bet size (10, 20, 50, 100):"))
            if bet > player_chips:
                print("You do not have enough chips.")
            elif bet not in [10, 20, 50, 100]:
                print("Choose a valid bet size.")
            else:
                break
        except ValueError:
            print("Enter a valid number.")

    player_chips -= bet

    # presentation helpers (no game logic)
    def card_to_str(card_tuple):
        rank, suit = card_tuple
        return f"{rank}{suit}"

    def hand_to_str(hand, hide_hole=False):
        if hide_hole and len(hand) >= 2:
            visible = [card_to_str(hand[0]), "[hidden]"]
            if len(hand) > 2:
                visible += [card_to_str(c) for c in hand[2:]]
            return ", ".join(visible)
        return ", ".join(card_to_str(c) for c in hand)

    def score_to_str(score_tuple):
        total, is_soft = score_tuple
        return f"{total} ({'soft' if is_soft else 'hard'})"

    def show_state(label, hand, score, hide_hole=False):
        print(f"{label}: {hand_to_str(hand, hide_hole)} → {score_to_str(score)}")

    # --- dealing functions ---
    def draw_player_cards():
        player_first_card_tuple = deck_tuples.pop()
        player_second_card_tuple = deck_tuples.pop()
        player_hand_in_function = [player_first_card_tuple, player_second_card_tuple]
        return player_hand_in_function

    def draw_dealer_cards():
        dealer_cards_first_tuples = deck_tuples.pop()
        dealer_cards_second_tuples = deck_tuples.pop()
        dealer_hand_in_function = [dealer_cards_first_tuples, dealer_cards_second_tuples]
        return dealer_hand_in_function

    def deal_player_single_card(player_hand):
        player_first_card_tuple = deck_tuples.pop()
        player_hand.append(player_first_card_tuple)

    def deal_dealer_single_card(dealer_hand):
        dealer_first_card_tuple = deck_tuples.pop()
        dealer_hand.append(dealer_first_card_tuple)

    # --- scoring functions (ace-aware) ---
    def player_hand_scoring(player_hand):
        player_aces_counter = 0
        player_hand_score = 0
        for rank, suit in player_hand:
            if rank in ('J', 'Q', 'K'):
                player_hand_score += 10
            elif rank == 'A':
                player_aces_counter += 1
            else:
                player_hand_score += int(rank)
        total = player_hand_score + 11 * player_aces_counter
        aces_as_eleven = player_aces_counter
        while total > 21 and aces_as_eleven > 0:
            total -= 10
            aces_as_eleven -= 1
        is_soft = (aces_as_eleven > 0)
        return total, is_soft

    def dealer_hand_scoring(dealer_hand):
        dealer_aces_counter = 0
        dealer_hand_score = 0
        for rank, suit in dealer_hand:
            if rank in ('J', 'Q', 'K'):
                dealer_hand_score += 10
            elif rank == 'A':
                dealer_aces_counter += 1
            else:
                dealer_hand_score += int(rank)
        total = dealer_hand_score + 11 * dealer_aces_counter
        aces_as_eleven = dealer_aces_counter
        while total > 21 and aces_as_eleven > 0:
            total -= 10
            aces_as_eleven -= 1
        is_soft = (aces_as_eleven > 0)
        return total, is_soft

    # initial deal and scoring (show working)
    player_hand = draw_player_cards()
    player_score = player_hand_scoring(player_hand)
    show_state("PLAYER", player_hand, player_score)

    dealer_hand = draw_dealer_cards()
    dealer_score = dealer_hand_scoring(dealer_hand)
    show_state("DEALER", dealer_hand, dealer_score)  # or hide_hole=True

    # immediate round checks: natural blackjacks (both first)
    player_has_blackjack = (player_score[0] == 21 and len(player_hand) == 2)
    dealer_has_blackjack = (dealer_score[0] == 21 and len(dealer_hand) == 2)

    if player_has_blackjack and dealer_has_blackjack:
        draw = True
    elif player_has_blackjack:
        player_win = True
    elif dealer_has_blackjack:
        dealer_win = True
    else:
        player_second_turn = True  # move to player action phase

    # player action loop (hit/stand)
    while player_second_turn:
        hit_or_stand = input("\nWould you like to Hit or Stand? ")
        if hit_or_stand.lower() == 'stand':
            player_second_turn = False
            break
        elif hit_or_stand.lower() == 'hit':
            deal_player_single_card(player_hand)
            player_score = player_hand_scoring(player_hand)
            show_state("PLAYER HIT", player_hand, player_score)
            if player_score[0] > 21:
                dealer_win = True
                player_second_turn = False
                break
        else:
            print("Please type 'Hit' or 'Stand'.")

    dealer_turn_active = False
    if not player_win and not dealer_win and not draw:
        dealer_turn_active = True

    while dealer_turn_active:
        dealer_score = dealer_hand_scoring(dealer_hand)
        dealer_total, dealer_soft = dealer_score
        if dealer_total > 21:
            player_win = True
            print("Dealer has gone bust.")
            break
        if dealer_total < 17:
            deal_dealer_single_card(dealer_hand)
            show_state("DEALER HIT", dealer_hand, dealer_score)
            continue
        if dealer_total == 17:
            dealer_turn_active = False
            show_state("DEALER STANDS (17)", dealer_hand, dealer_score)
        else:
            dealer_turn_active = False
            show_state("DEALER STANDS", dealer_hand, dealer_score)

    # final comparison (if needed)
    if not player_win and not dealer_win and not draw:
        player_score = player_hand_scoring(player_hand)
        dealer_score = dealer_hand_scoring(dealer_hand)
        if player_score[0] > dealer_score[0]:
            player_win = True
        elif dealer_score[0] > player_score[0]:
            dealer_win = True
        else:
            draw = True

    # payout
    def payout():
        nonlocal player_win, dealer_win, draw
        global player_chips
        if player_has_blackjack:
            player_chips += int(bet * 2.5)
        elif player_win:
            player_chips += bet * 2
        elif draw:
            player_chips += bet

    payout()

    # update JSON leaderboard
    player_data[username]["chips"] = player_chips
    player_data[username]["rounds_played"] += 1
    if player_win:
        player_data[username]["wins"] += 1
    save_player_data(player_data)

    # final output
    show_state("PLAYER FINAL", player_hand, player_score)
    show_state("DEALER FINAL", dealer_hand, dealer_score)
    print("RESULT:", "Player wins" if player_win else "Dealer wins" if dealer_win else "Push (draw)")
    print(f"Your current chips: ${player_chips}")

    # display leaderboard
    display_leaderboard()

    return player_win, dealer_win, draw

# --- game loop logic ---
game_running = True

while game_running:
    play_blackjack_round()

    play_again = input("\nWould you like to play a round of Blackjack? (yes/no)")
    if play_again.lower() == 'yes':
        deck_length = len(deck_tuples)
        if deck_length < 20:
            print("Cards are running low. Reshuffling...")
            deck_tuples = [(rank, suit) for suit in suits for rank in ranks]
            random.shuffle(deck_tuples)
        print("\nStarting a new round of Blackjack...\n")
        continue
    elif play_again.lower() == 'no':
        print("Thanks for playing! Goodbye.")
        game_running = False
        break
    else:
        print("\nInvalid input. Please type 'yes' or 'no'.")
        continue
