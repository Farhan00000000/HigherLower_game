# from art import logo, vs
# from game_data import data
# import random as ran
#
# good = False
# while not good:
#     print(logo)
#     rand_dict = ran.choice(data)
#     A = rand_dict
#     print(f"Compare A: {A['name']}, a {A['description']} and from {A['country']}.")
#
#     print(vs)
#
#     random_dict = ran.choice(data)
#     B = random_dict
#     print(f"Against B: {B['name']}, {B['description']} and {B['country']}.")
#
#     user = input("Who has more followers? Type 'A' or 'B': ")
#
#     A = A["follower_count"]
#     B = B["follower_count"]
#
#     print(f"A = {A}")
#     print(f"B = {B}")
#
#     if user == "A":
#         user = A
#
#         if A > B:
#             # print("Ok")
#
#             print("You're right! Current score: {}")
#
#         elif B > A:
#
#             print("No")
#
#             print("You're wrong! Current score: {}")
#
#             good = True
#
#     elif user == "B":
#         user = B
#
#         if B > A:
#             # print("Ok")
#
#             print("You're right! Current score: {}")
#
#         elif A > B:
#
#             print("No")
#
#             print("You're wrong! Current score: {}")
#
#             good = True
#
#     elif user == "A" or user == "B":
#         if A == B:
#             print("Draw")


from art import logo, vs
from game_data import data
import random


# from replit import clear


def formate_data(account):
    """Take the account data and return the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""

    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# display art
print(logo)
score = 0
game_should_continue = True

# Generate a random account from the game data.
account_b = random.choice(data)
# Make the game repeatable
while game_should_continue:

    # Make account at position B become the next account at position A

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {formate_data(account_a)}.")

    print(vs)

    print(f"Compare B: {formate_data(account_b)}.")

    # Ask user for guess.

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    # Get follower count of each account.

    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    # Clear the screen between rounds.
    # clear()
    print(logo)
    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, you're wrong. Final score: {score}.")
