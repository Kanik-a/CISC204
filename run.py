from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# These two lines make sure a faster SAT solver is used.
from nnf import config
config.sat_backend = "kissat"
# Create an encoding to store constraints
E = Encoding()
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def prop_name(self):
        return f"A.{self.data}"
# Define basic propositions for the Uno game
C = BasicPropositions("C")  # Previous card and the card in players hand have the same colour
T = BasicPropositions("T")  # Previous card and the card in players hand have the same number
B = BasicPropositions("B")  # Player has a card that can be played
E2 = BasicPropositions("E2") # Previous card is a draw 2 card
F = BasicPropositions("F")  # Previous card is a draw 4 card
R = BasicPropositions("R")  # Previous card is a reverse card
S = BasicPropositions("S")  # Previous card is a skip card
U = BasicPropositions("U")  # Player has met the winning condition
W = BasicPropositions("W")  # Wild card can be played
A = BasicPropositions("A")  # Player has cards in hand
D = BasicPropositions("D")  # Player has to draw a card

# Define a fancy proposition for checking if a card can be played
prop = [C,T,B,E2,F,R,S,U,W,A,D]
@constraint.at_least_one(E)
@proposition(E)
class FancyProposition:

    def __init__(self, data):
        self.data = data

    def _prop_name(self):
        return f"Playable.{self.data}"

x = FancyProposition("x")
def uno_constraints():
    
    # Add constraints for the playable condition
    E.add_constraint(B >> (C | T))                # B implies C or T
    E.add_constraint(A & (C | T | W) >> B)        # A and (C or T or W) implies B
    E.add_constraint((R | S) >> ~B)                # (R or S) implies not B
    E.add_constraint((F | E2) >> (D | B))           # (F or E) implies (D or B)
    E.add_constraint(~A >> U)                      # not A implies U
    E.add_constraint(~B >> D)                      # not B implies D
    E.add_constraint(W >> (C | T) & ~(C | T)) 

    # At least one of the previous card conditions must be true
    #E.add_constraint(constraint.at_least_one(E2))

    return E

if __name__ == "__main__":

    T = uno_constraints()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([C,T,B,E2,F,R,S,U,W,A,D], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()