"""
BLACKJACK — SIMPLE PROGRAMMING BREAKDOWN (Learning Notes)

-------------------------------------
1) DATA TO REPRESENT
-------------------------------------
- Card: rank + suit (example: 'A♠' or ('A','Spades'))
- Deck: list of 52 cards; shuffle with random.shuffle()
- Hand: list of cards (player hand, dealer hand)
- Bankroll: integer for chips (start simple — could even skip at first)

-------------------------------------
2) BASIC RULES TO TURN INTO CODE
-------------------------------------
- Game starts: shuffle deck, deal 2 cards each (player & dealer)
- Player goes first:
    * HIT = add another card
    * STAND = stop taking cards
    * (Optional later: DOUBLE or SPLIT)
- Dealer plays:
    * Dealer draws until total >= 17
- Scoring hands:
    * J/Q/K = 10
    * A = 1 or 11 (whichever helps without busting)
    * Other cards = face value
- Results:
    * If player busts (>21) → dealer wins
    * If dealer busts → player wins
    * Else compare totals:
        higher total wins, equal = push (tie)

-------------------------------------
3) FUNCTIONS YOU'LL NEED
-------------------------------------
- build_deck() → returns list of 52 cards
- shuffle_deck(deck) → shuffles list
- deal_card(deck, hand) → pops card from deck into a hand
- hand_value(hand) → calculates total with Ace as 1 or 11
- is_blackjack(hand) → True if exactly 2 cards totaling 21
- play_dealer(hand, deck) → dealer hits until 17+

-------------------------------------
4) GAME FLOW (STATE MACHINE — SIMPLE)
-------------------------------------
1. Build and shuffle deck
2. Deal two cards each
3. Check for blackjack (instant win/loss/push)
4. Player turn (while loop: hit or stand)
5. Dealer turn (dealer auto-plays)
6. Compare totals → print winner
7. Ask: play again? If yes, repeat

-------------------------------------
5) EDGE CASES (ADD LATER)
-------------------------------------
- Multiple Aces in one hand (hand_value must handle this)
- Dealer soft 17 (decide hit or stand)
- Splits, double, surrender (skip at first!)
- Betting and bankroll tracking (can add once basic game works)

-------------------------------------
6) GOOD HABITS
-------------------------------------
- Keep card math (hand_value) separate from input/output
- Test hand_value() by giving it fake hands (like ['A','K'])
- Use small, clear functions
- Dont try to code every rule at once — add features step by step

-------------------------------------
BUILD STRATEGY
1. Make a deck + shuffle + deal two cards
2. Write hand_value() to calculate totals
3. Add player hit/stand loop
4. Add dealer logic
5. Add win/lose logic
6. Later: add bets, splits, doubles, and other rules

"""
import random

# game state flags
round_active = True
player_win = False
dealer_win = False
draw = False
player_second_turn = False

# card definitions
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['♠', '♥', '♦', '♣']

# build deck as tuples
deck_tuples = [(rank, suit) for suit in suits for rank in ranks]
# Example: ('A', '♠'), ('10', '♥'), ('K', '♦')
random.shuffle(deck_tuples)

# presentation helpers (no game logic)

def card_to_str(card_tuple):
    rank, suit = card_tuple
    return f"{rank}{suit}"

def hand_to_str(hand, hide_hole=False):
    if hide_hole and len(hand) >= 2:
        visible = [card_to_str(hand[0]), "[hidden]"]
        # if dealer later has more cards, show them after the hidden marker
        if len(hand) > 2:
            visible += [card_to_str(c) for c in hand[2:]]
        return ", ".join(visible)
    return ", ".join(card_to_str(c) for c in hand)

def score_to_str(score_tuple):
    total, is_soft = score_tuple
    return f"{total} ({'soft' if is_soft else 'hard'})"

def show_state(label, hand, score, hide_hole=False):
    print(f"{label}: {hand_to_str(hand, hide_hole)}  →  {score_to_str(score)}")

# --- dealing functions ---

def draw_player_cards():
    # draw 2 cards for the player from the (already shuffled) deck
    player_first_card_tuple = deck_tuples.pop()
    player_second_card_tuple = deck_tuples.pop()
    player_hand_in_function = [player_first_card_tuple, player_second_card_tuple]
    return player_hand_in_function

def draw_dealer_cards():
    # draw 2 cards for the dealer from the (already shuffled) deck
    dealer_cards_first_tuples = deck_tuples.pop()
    dealer_cards_second_tuples = deck_tuples.pop()
    dealer_hand_in_function = [dealer_cards_first_tuples, dealer_cards_second_tuples]
    return dealer_hand_in_function

def deal_player_single_card(player_hand):
    # hit: deal one card to the existing player hand (mutates in-place)
    player_first_card_tuple = deck_tuples.pop()
    player_hand.append(player_first_card_tuple)

def deal_dealer_single_card(dealer_hand):
    # hit: deal one card to the existing dealer hand (mutates in-place)
    dealer_first_card_tuple = deck_tuples.pop()
    dealer_hand.append(dealer_first_card_tuple)

# --- scoring functions (ace-aware) ---

def player_hand_scoring(player_hand):
    # returns (total, is_soft) for the player's hand
    player_aces_counter = 0
    player_hand_score = 0  # sum of non-ace ranks (numbers + face cards)

    for rank, suit in player_hand:
        if rank in ('J', 'Q', 'K'):
            player_hand_score += 10
        elif rank == 'A':
            player_aces_counter += 1
        else:
            player_hand_score += int(rank)

    # Start total by adding all Aces as 11
    total = player_hand_score + 11 * player_aces_counter
    aces_as_eleven = player_aces_counter

    # Demote Aces from 11 -> 1 while busting
    while total > 21 and aces_as_eleven > 0:
        total -= 10
        aces_as_eleven -= 1

    is_soft = (aces_as_eleven > 0)
    return total, is_soft

def dealer_hand_scoring(dealer_hand):
    # returns (total, is_soft) for the dealer's hand
    dealer_aces_counter = 0
    dealer_hand_score = 0  # sum of non-ace ranks (numbers + face cards)

    for rank, suit in dealer_hand:
        if rank in ('J', 'Q', 'K'):
            dealer_hand_score += 10
        elif rank == 'A':
            dealer_aces_counter += 1
        else:
            dealer_hand_score += int(rank)

    # Start total by adding all Aces as 11
    total = dealer_hand_score + 11 * dealer_aces_counter
    aces_as_eleven = dealer_aces_counter

    # Demote Aces from 11 -> 1 while busting
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
# If you want to hide dealer hole card initially, set hide_hole=True
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
        # deal one card to player, then re-score and check bust immediately
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
# checking if dealer plays after player does
if player_win == False and dealer_win == False and draw == False:
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
        show_state("DEALER HIT", dealer_hand, dealer_score)  # score shown next loop
        continue

    if dealer_total == 17:
        dealer_turn_active = False
        show_state("DEALER STANDS (17)", dealer_hand, dealer_score)
    else:
        # 18, 19, 20, 21
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

# final output

show_state("PLAYER FINAL", player_hand, player_score)
show_state("DEALER FINAL", dealer_hand, dealer_score)
print("RESULT:", "Player wins" if player_win else "Dealer wins" if dealer_win else "Push (draw)")
