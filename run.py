from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# These two lines make sure a faster SAT solver is used.
from nnf import config
config.sat_backend = "kissat"

# Encoding that will store all of your constraints
E = Encoding()

# Define propositions for different conditions of the cards and the game
@proposition(E)
class CardPropositions:
    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"Card.{self.data}"

# Define the propositions for the player's cards
A = CardPropositions("A")  # Player has cards in hand
C = CardPropositions("C")  # Current card matches the color of the previous card
N = CardPropositions("N")  # Current card matches the color of the previous card
R = CardPropositions("R")  # Previous Card is a Reverse card
S = CardPropositions("S")  # Previous Card is a Skip card
D2 = CardPropositions("D2")  # Previous Card is a Draw2 card
D4 = CardPropositions("D4")  # Previous Card is a Draw4 card
W = CardPropositions("W")  # Card is a wild card
Game_Ended = CardPropositions("GameEnded")  # Game has ended

# Color proposition to check if the cards currently in players hand are a specific color or not.
@constraint.exactly_one(E)
@proposition(E)
class ColorPropositions():
    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"Color.{self.data}"
# Current Card in player's hand is either red, blue, green or yellow in color
CCR = ColorPropositions("CCR") 
CCB = ColorPropositions("CCB") 
CCG = ColorPropositions("CCG") 
CCY = ColorPropositions("CCY") 

# Color proposition to check if the cards currently in players hand are a specific number/icon[0-9, draw4, wild, draw2, skip] or not.
@constraint.exactly_one(E)
@proposition(E)
class NumberPropositions():
    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"Number.{self.data}"
    
# Current card in player's hand has number [0-9], wild, draw2, draw4 or skip
CN0 = NumberPropositions("CN0") 
CN1 = NumberPropositions("CN1") 
CN2 = NumberPropositions("CN2") 
CN3 = NumberPropositions("CN3") 
CN4 = NumberPropositions("CN4") 
CN5 = NumberPropositions("CN5") 
CN6 = NumberPropositions("CN6") 
CN7 = NumberPropositions("CN7") 
CN8 = NumberPropositions("CN8") 
CN9 = NumberPropositions("CN9") 
CNS = NumberPropositions("CNS") 
CND4 = NumberPropositions("CND4")
CND2 = NumberPropositions("CND2") 
CNW = NumberPropositions("CNW") 

# Previous Color proposition to check if the cards played previously are a specific color or not.
@constraint.exactly_one(E)
@proposition(E)
class PrevColorPropositions():
    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"PrevColor.{self.data}"
# Previous card is either red, blue, green or yellow in color.
PCCR = PrevColorPropositions("PCCR")
PCCB = PrevColorPropositions("PCCB")
PCCG = PrevColorPropositions("PCCG")
PCCY = PrevColorPropositions("PCCY")

# Previous Number proposition to check if the cards played previously are a specific number/icon or not.
@constraint.exactly_one(E)
@proposition(E)
class PrevNumberPropositions():
    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"PrevNumber.{self.data}"
# Previous card has either 0-9, skip, draw4, draw2, wild
PCN0 = PrevNumberPropositions("PCN0") # Card has number 0
PCN1 = PrevNumberPropositions("PCN1") # Card has number 1
PCN2 = PrevNumberPropositions("PCN2") # Card has number 2
PCN3 = PrevNumberPropositions("PCN3") # Card has number 3
PCN4 = PrevNumberPropositions("PCN4") # Card has number 4
PCN5 = PrevNumberPropositions("PCN5") # Card has number 5
PCN6 = PrevNumberPropositions("PCN6") 
PCN7 = PrevNumberPropositions("PCN7") # Card has number 7
PCN8 = PrevNumberPropositions("PCN8") # Card has number 8
PCN9 = PrevNumberPropositions("PCN9") # Card has number 9
PCNS = PrevNumberPropositions("PCNS") # Card is a skip card
PCND4 = PrevNumberPropositions("PCND4") # Card is a Draw4 card
PCND2 = PrevNumberPropositions("PCND2") # Card is a Draw2 card
PCNW = PrevNumberPropositions("PCNW") # Card is a wild card

# Proposition to check if we can accumulate draw2 cards
@proposition(E)
class CanAccumulateD2:
    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"CanAccumulateD2.{self.data}"

# Proposition to check if we can accumulate draw4 cards
@proposition(E)
class CanAccumulateD4:
    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"CanAccumulateD4.{self.data}"
    
# Proposition to check if we can draw multiple cards
@proposition(E)
class MustDrawMultiple:
    def __init__(self, data):
        self.data = data
    
    def _prop_name(self):
        return f"MustDrawMultiple.{self.data}"
    
# # Proposition to check if we can play a card
@constraint.at_least_one(E)
@proposition(E)
class CanPlay:
    def __init__(self, data):
        self.data = data
    
    def _prop_name(self):
        return f"CanPlay.{self.data}"
can_accumulate_d2 = CanAccumulateD2("can_accumulate_d2")    
can_accumulate_d4 = CanAccumulateD4("can_accumulate_d4")   
must_draw_multiple = MustDrawMultiple("must_draw_multiple") 
can_play = CanPlay("can_play")


'''previous_cards holds info[color, number] about the cards previously played one after another. In the code the cards are 
fetched one after another and appended to a list and then evaluated to see if their values hold true or not'''
previous_cards = [
    {'color':'yellow', 'number':'3'},
    {'color': 'red', 'number': '3'},
    {'color': 'blue', 'number': 'skip'},
    {'color': 'green', 'number': '2'},
    {'color': 'yellow', 'number': '8'},
    {'color': 'black','number': 'draw4'},
    {'color': 'green', 'number': '5'}
]
'''current_card holds info[color, number] about all the cards currently in the players hand. While only one card from the
list previous_cards is taken into account at once, all cards in current_cards are considered at all times in the same way we 
would have in a real game.'''
current_cards = [
    {'color': 'red', 'number': 'draw2'},
    {'color': 'blue', 'number': '3'},
    {'color': 'green', 'number': '0'},
    {'color': 'black', 'number': 'draw4'},
    {'color': 'red', 'number': 'skip'},
    {'color': 'green', 'number': '8'},
    {'color': 'blue', 'number': '1'},
]

# Function to check which color and number a card currently in the player's hand is.
def current_matching_color_number(current_cards):
    """
    Adds and manages constraints for matching the current card's color or number.
    :param current_cards: List of dictionaries representing current cards in player's hand with 'color' and 'number' keys.
    """
    current_card_constraints = [] # list to store the contraints if true
    for item in current_cards:
       
            # Checking color and add the corresponding color constraint
            if item['color'] == 'red':
                current_card_constraints.append(CCR)
                E.add_constraint(CCR)
            elif item['color'] == 'blue':
                current_card_constraints.append(CCB)
                E.add_constraint(CCB)
            elif item['color'] == 'green':
                current_card_constraints.append(CCG)
                E.add_constraint(CCG)
            elif item['color'] == 'yellow':
                current_card_constraints.append(CCY)
                E.add_constraint(CCY)
        
            # Checking number and add the corresponding number constraint
            if item['number'] == '0':
                current_card_constraints.append(CN0)
                E.add_constraint(CN0)
            elif item['number'] == '1':
                current_card_constraints.append(CN1)
                E.add_constraint(CN1)
            elif item['number'] == '2':
                current_card_constraints.append(CN2)
                E.add_constraint(CN2)
            elif item['number'] == '3':
                current_card_constraints.append(CN3)
                E.add_constraint(CN3)
            elif item['number'] == '4':
                current_card_constraints.append(CN4)
                E.add_constraint(CN4)
            elif item['number'] == '5':
                current_card_constraints.append(CN5)
                E.add_constraint(CN5)
            elif item['number'] == '6':
                current_card_constraints.append(CN6)
                E.add_constraint(CN6)
            elif item['number'] == '7':
                current_card_constraints.append(CN7)
                E.add_constraint(CN7)
            elif item['number'] == '8':
                current_card_constraints.append(CN8)
                E.add_constraint(CN8)
            elif item['number'] == '9':
                current_card_constraints.append(CN9)
                E.add_constraint(CN9)
            elif item['number'] == 'draw4':
                current_card_constraints.append(CND4)
                E.add_constraint(CND4)
            elif item['number'] == 'draw2':
                current_card_constraints.append(CND2)
                E.add_constraint(CND2)
            elif item['number'] == 'skip':
                current_card_constraints.append(CNS)
                E.add_constraint(CNS)
            elif item['number'] == 'wild':
                current_card_constraints.append(CNW)
                E.add_constraint(CNW)
    return current_card_constraints
print(current_matching_color_number(current_cards))


def can_play_card(temporary_constraints, current_card_constraints):
    '''Function to check if a card is playable. This depends on whether the color or number of any of the current card 
    matches the previous card'''
    try:
        added_constraints_set = set(temporary_constraints)  
    except TypeError:
        added_constraints_set = {tuple(x.items()) if isinstance(x, dict) else x for x in temporary_constraints}

    # Match current and previous cards for valid play (for color)
    for color, prev_color in zip([CCR, CCB, CCG, CCY], [PCCR, PCCB, PCCG, PCCY]):
        if color in current_card_constraints and prev_color in added_constraints_set:
            E.add_constraint((color & prev_color) >> C)

    # Match current and previous cards for valid play (for number)
    for number, prev_number in zip(
        [CN0, CN1, CN2, CN3, CN4, CN5, CN6, CN7, CN8, CN9, CND2, CND4, CNS, CNW],
        [PCN0, PCN1, PCN2, PCN3, PCN4, PCN5, PCN6, PCN7, PCN8, PCN9, PCND2, PCND4, PCNS, PCNW]
    ):
        if number in current_card_constraints and prev_number in added_constraints_set:
            E.add_constraint((number & prev_number) >> N)

    # Check if color or number match (using C and N propositions)
    color_match = any(color in current_card_constraints for color in [CCR, CCB, CCG, CCY])
    number_match = any(number in current_card_constraints for number in [CN0, CN1, CN2, CN3, CN4, CN5, CN6, CN7, CN8, CN9, CND2, CND4, CNS, CNW])

    # If either color or number match, player can play
    if color_match or number_match:
        E.add_constraint((C | N) >> can_play)  # If either color or number is satisfied, player can play
    else:
        E.add_constraint(~(C | N) >> ~can_play)  # If neither is satisfied, player cannot play


# Function to check which color and number a previously played card is.
def prev_matching_color_number(previous_cards):
    """
    Adds and manages constraints for matching the previous card's color or number.
    :param previous_cards: List of dictionaries representing previous cards with 'color' and 'number' keys.
    """
    color_constraints = {
        'red': PCCR,
        'blue': PCCB,
        'green': PCCG,
        'yellow': PCCY
    }
    number_constraints = {
        '0': PCN0, '1': PCN1, '2': PCN2, '3': PCN3, '4': PCN4,
        '5': PCN5, '6': PCN6, '7': PCN7, '8': PCN8, '9': PCN9,
        'skip': PCNS, 'draw4': PCND4, 'draw2': PCND2
    }

    temporary_constraints = []

    for card in previous_cards:
        # Adding color constraints if valid
        if card['color'] in color_constraints:
            constraint = color_constraints[card['color']]
            E.add_constraint(constraint)
            temporary_constraints.append(constraint)

        # Adding number constraints if valid
        if card['number'] in number_constraints:
            constraint = number_constraints[card['number']]
            E.add_constraint(constraint)
            temporary_constraints.append(constraint)

    can_play_card(temporary_constraints, temporary_constraints)

    for constraint in temporary_constraints:
        E.clear_constraints()

print(prev_matching_color_number(previous_cards))



def can_accumulate_d2_card(temporary_constraints, current_card_constraints):
    '''Check if the previous card is a draw2 and whether the player has a draw2 in hand, if so draw2's can be accumulated
    :param temporary_constraints[list], current_card_constraints[list]: both lists contain the constraints pertaining 
    to which color and number is on the previous and current cards. '''
    prev_cnd2_exists = PCND2 in temporary_constraints
    cnd2_exists = CND2 in current_card_constraints

    if prev_cnd2_exists and cnd2_exists:
        E.add_constraint((PCND2 & CND2) >> can_accumulate_d2) 
    else:
        E.add_constraint(~can_accumulate_d2)

        
def can_accumulate_d4_card(temporary_constraints, current_card_constraints):
    '''Check if the previous card is a draw4 and whether the player has a draw4 in hand, if so draw4's can be accumulated
    :param temporary_constraints[list], current_card_constraints[list]: both lists contain the constraints pertaining 
    to which color and number is on the previous and current cards. '''
    prev_cnd4_exists = PCND4 in temporary_constraints  
    cnd4_exists = CND4 in current_card_constraints  
    
    if prev_cnd4_exists and cnd4_exists:
        E.add_constraint((PCND4 & CND4) >> 'can_accumulate_d4') 
    else:
        E.add_constraint(~'can_accumulate_d4')


def example_theory():
    
    E.add_constraint((C | N) >> can_play)
    E.add_constraint(~(C|N) >> ~can_play)
    E.add_constraint(W >> can_play)
    E.add_constraint((PCND2 & CND2) >> can_accumulate_d2)  
    E.add_constraint((PCND4 & CND4) >> can_accumulate_d4)    
    E.add_constraint(D4 >> can_play)
    E.add_constraint(R|S >> ~can_play)  # Can't play if the card is a Reverse
    E.add_constraint(PCND2 & ~can_accumulate_d2 >> must_draw_multiple)
    E.add_constraint(PCND4 & ~can_accumulate_d4 >> must_draw_multiple)
    E.add_constraint(~A >> Game_Ended)

    

    return E


if __name__ == "__main__":
    T = example_theory()
    # Compile the theory
    T = T.compile()
    # After compilation (and only after), you can check the properties
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v, vn in zip([A, C, N, R, S, D2, D4, W, Game_Ended], 'ACNRSDWG'):
        print(f" {vn}: %.2f" % likelihood(T, v))
    print()
