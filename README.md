Blackjack Game

A simple terminal-based Blackjack game written in Python.

Made for Week 2 of Specialisterne Academy.

🎮 Features

Play against the dealer in a game of Blackjack.

Betting system with balance tracking.

🛠️ Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/blackjack-game.git
cd blackjack-game

2️⃣ Install Dependencies

Ensure you have Python installed (>=3.8)

3️⃣ Run the Game

python main.py

🔨 Build as Executable (Optional)

To create a standalone executable:

pyinstaller --onefile --noconsole --icon=game.ico main.py

The .exe file will be in the dist/ folder.

🎯 Game Rules

The goal is to get as close to 21 as possible without going over.

Face cards (J, Q, K) are worth 10.

Aces (A) can be 1 or 11, depending on what benefits the hand.

If your hand exceeds 21, you lose (BUST).

The dealer stands on 17 or higher.

📜 Code Structure

blackjack-game/
│-- main.py             # Entry point of the game
│-- player.py           # Player class
│-- dealer.py           # Dealer class
│-- card.py             # Card and Deck management
│-- game.py             # Game logic and flow
│-- utils.py            # Helper functions
│-- README.md           # Project documentation
