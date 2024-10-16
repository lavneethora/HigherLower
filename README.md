# Higher or Lower: Instagram Followers Edition

This is a Python-based CLI game where you guess which Instagram user has more followers. It's based on a dataset of Instagram profiles, and their follower counts are retrieved in real-time using the `Instaloader` library. The game continues until you make a wrong guess.

## Project Files

- **main.py**: The main game logic. It picks two Instagram profiles at random from a dataset and asks the player to guess which one has more followers.
- **art.py**: Contains ASCII art for the game logo and versus separator.
- **lists.py**: Contains the dataset of Instagram profiles used in the game.

## How the Game Works

1. Two random Instagram profiles are chosen from a predefined dataset.
2. The user has to guess which one has more followers.
3. If the guess is correct, the user's score increases and the game continues.
4. If the guess is incorrect, the game ends and the final score is displayed.

## Dependencies

This project uses the following dependencies:
- `instaloader`: A Python library for interacting with Instagram. It is used to retrieve follower counts in real-time.
- `random`: A standard Python library to pick random profiles from the dataset.
- `time`: For adding a slight delay between rounds.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HigherLower.git
   ```
2. Install the required Python packages:
   ```bash
   pip install instaloader
   ```

## Running the Game

- To start the game, run the following command:
   ```bash
   python main.py
   ```

## Example

```bash
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/              
           
Compare A: Person A, Celebrity, from USA
  vs
Compare B: Person B, Influencer, from UK

Who has more followers? Type 'A' or 'B': A
You're right! Person A has more followers.
Current score: 1
```

## Dataset

- The dataset used for the game is stored in lists.py and includes a list of dictionaries. Each dictionary contains details about a profile such as:
  - username: Instagram username of the person
  - name: Name of the person
  - description: Description of the person (e.g., celebrity, influencer)
  - country: The person's country

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
- Feel free to submit issues or pull requests for any improvements or bug fixes.

## Author

- Lavneet Hora
- Sophomore @ Texas Tech University
- Computer Science
