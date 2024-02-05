# Connect4_with_pygame

Welcome to the Connect Four game for two players playing on the same computer!

## Implementation

This game is implemented using Python and the Pygame library. Below is a brief overview of the code structure:

- **Main Script:** The main script is `connect_four.py`. It initializes the Pygame library, sets up the game window, and contains the game loop.

- **Game Classes:**
  - **Red_bead and Yellow_bead:** Represent the red and yellow beads on the board. They handle the animation of falling beads.
  - **ARROW:** Represents the arrow buttons for column selection. It handles user input for column selection.
  - **Reset:** Manages the "RESTART" button, allowing players to reset the game.

- **Check Functions:** The `row`, `column`, and `dia` functions generate lists of possible winning combinations in rows, columns, and diagonals. The `checkend` function checks for a winning combination or a draw.

- **Game Flow:** The game flow is managed using the game loop. Players take turns throwing beads into the board by clicking on the arrow buttons. The game ends when a player connects four beads or when the board is filled.

## How to Run

1. Install Python 3.x on your computer.
2. Install the Pygame library by running the following command in your terminal:
3. Run the Python script to start the game:


## Code Description

- The code utilizes Pygame for creating the game window, handling user input, and displaying graphics.

- Beads fall smoothly into the chosen column using animation implemented in the Red_bead and Yellow_bead classes.

- ARROW class handles user input for column selection, allowing players to click on the arrows to drop beads.

- The game state is updated in the game loop, and the screen is continuously redrawn to reflect the current state of the game.

- The game logic, including checking for winning combinations and handling restarts, is implemented in an organized manner.

Have fun exploring the code and playing Connect Four!
