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

## Structure

* `documents`: Contains folders for both of our draft and final submissions. README.md files are included in both.
* `run.py`: General wrapper script that you can choose to use or not. Only requirement is that you implement the one function inside of there for the auto-checks.
* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.

## Running With Docker

By far the most reliable way to get things running is with [Docker](https://www.docker.com). This section runs through the steps and extra tips to running with Docker. You can remove this section for your final submission, and replace it with a section on how to run your project.

1. First, download Docker https://www.docker.com/get-started

2. Navigate to your project folder on the command line.

3. We first have to build the course image. To do so use the command:
`docker build -t cisc204 .`

4. Now that we have the image we can run the image as a container by using the command: `docker run -it -v $(pwd):/PROJECT cisc204 /bin/bash`

    `$(pwd)` will be the current path to the folder and will link to the container

    `/PROJECT` is the folder in the container that will be tied to your local directory

5. From there the two folders should be connected, everything you do in one automatically updates in the other. For the project you will write the code in your local directory and then run it through the docker command line. A quick test to see if they're working is to create a file in the folder on your computer then use the terminal to see if it also shows up in the docker container.

### Mac Users w/ M1 Chips

If you happen to be building and running things on a Mac with an M1 chip, then you will likely need to add the following parameter to both the build and run scripts:

```
--platform linux/x86_64
```

For example, the build command would become:

```
docker build --platform linux/x86_64 -t cisc204 .
```

### Mount on Different OS'

In the run script above, the `-v $(pwd):/PROJECT` is used to mount the current directory to the container. If you are using a different OS, you may need to change this to the following:

- Windows PowerShell: `-v ${PWD}:/PROJECT`
- Windows CMD: `-v %cd%:/PROJECT`
- Mac: `-v $(pwd):/PROJECT`

Finally, if you are in a folder with a bunch of spaces in the absolute path, then it will break things unless you "quote" the current directory like this (e.g., on Windows CMD):

```
docker run -it -v "%cd%":/PROJECT cisc204
```
