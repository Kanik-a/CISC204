# CISC/CMPE 204 Modelling Project 09: Winning UNO

This project models a simulation of a well-known card game, UNO. In this version of UNO, the player starts with 7 cards in their hand and must play one of these cards depending on the previously played card (i.e. the top card). This is determined through the colour and number or icon of the top card. A card is playable if one of the following holds:
- The colour of the card matches the colour of the top card;
- The number/icon of the card matches the number/icon of the top card; or
- They have a wildcard, in which case they can place it down whenever they want.

Otherwise, the player must draw another card from the deck.
Additionally, UNO has certain action cards:
- **Skip**: if a player places down a Skip card, then the next player’s turn is skipped.
- **Reverse**: if a player places down a Reverse card, then the order in which the people play reverses, and it becomes the previous player’s turn again.
- **Draw 2**: if a player places down a Draw 2 card, then the next player must draw 2 cards from the deck and misses their turn. However, if the next player also has a Draw 2 card, then they can place this card instead of drawing to accumulate the number of Draw 2 cards to the next player (i.e. the next player will have to draw 4 cards).
- **Draw 4 (Wild)**: similar rules apply here; however, not only does the next player have to draw 4 cards from the deck, but the current player can also change the current colour of the game.
- **Wild card**: if a player places down a “normal” wild card, then they can change the current colour of the game.

The objective of this game is to get rid of all of one’s cards first, which is something the code will determine. However, in our model, we will deem the sequence of play satisfiable and the game ended as long as the player loses all of their cards at the end.

If further clarification on the rules is needed, a more detailed overview of the game can be found here: https://en.wikipedia.org/wiki/Uno_(card_game)

## Structure

* `documents`: Contains folders for both of our draft and final submissions. README.md files are included in both.
* `run.py`: Main script, contains all of our functions.
* `test.py`: Run this file to confirm that our submission has everything required. This essentially just means it will check for the right files and sufficient theory size.
