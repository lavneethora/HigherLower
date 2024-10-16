import random
from art import higher_lower_logo
from art import higher_lower_vs
import instaloader
from time import sleep
from lists import higher_lower_dataset

L = instaloader.Instaloader()

def get_follower_count(username):
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        return profile.followers
    except Exception as e:
        print(f"Error fetching data for {username}: {e}")
        return None

score_count = 0
game_loop = True

print(higher_lower_logo)

while game_loop:
    player_a = random.choice(higher_lower_dataset)
    player_b = random.choice(higher_lower_dataset)

    while player_a == player_b:
        player_b = random.choice(higher_lower_dataset)

    player_a['follower_count'] = get_follower_count(player_a['username'])
    player_b['follower_count'] = get_follower_count(player_b['username'])

    if player_a['follower_count'] is None or player_b['follower_count'] is None:
        print("Could not retrieve follower data. Exiting game.")
        break

    print(f"\nCompare A: {player_a['name']}, {player_a['description']}, from {player_a['country']}")
    print(higher_lower_vs)
    print("\n")
    print(f"Compare B: {player_b['name']}, {player_b['description']}, from {player_b['country']}\n")


    guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

    if guess == 'A':
        if player_a['follower_count'] > player_b['follower_count']:
            score_count += 1
            print(f"You're right! {player_a['name']} has more followers.")
            print(f"Current score: {score_count}\n")
        else:
            print(f"Sorry, you're wrong. {player_b['name']} has more followers.")
            print(f"Final score: {score_count}")
            game_loop = False
    elif guess == 'B':
        if player_b['follower_count'] > player_a['follower_count']:
            score_count += 1
            print(f"You're right! {player_b['name']} has more followers.")
            print(f"Current score: {score_count}\n")
        else:
            print(f"Sorry, you're wrong. {player_a['name']} has more followers.")
            print(f"Final score: {score_count}")
            game_loop = False
    else:
        print("Invalid input. Please type 'A' or 'B'.")
        game_loop = False

    sleep(0.01)

print("Thanks for playing!")