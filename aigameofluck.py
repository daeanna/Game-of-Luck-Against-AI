#! /usr/she/bang/env python3
import random
import time

def roll_dice():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)

def brew_potion(skill):
    """Simulate brewing a magical potion based on player or AI skill."""
    potion_quality = skill + roll_dice()
    return potion_quality

def random_event():
    """Generate a random event during the game."""
    events = [
        "A mischievous pixie messes up your ingredients but you manage to salvage the potion.",
        "You discover a rare magical herb, enhancing the quality of your potion.",
        "The AI accidentally spills a potion, setting off colorful sparks in the room.",
        "You find a mysterious scroll with a secret potion recipe.",
    ]
    return random.choice(events)

def potion_race():
    """Allow the player and AI to race against time to create a potion."""
    ingredients = ["Winged Newt Eye", "Moonstone Powder", "Dragon Scale", "Phoenix Feather"]

    print("\nIngredient List:")
    print(", ".join(ingredients))

    player_time_limit = 10  # seconds
    ai_time_limit = 8  # seconds

    print(f"\n{'='*30}")
    print("     POTION RACE STARTS!     ")
    print(f"{'='*30}\n")

    print(f"\nYou have {player_time_limit} seconds to enter ingredients.")
    player_input = input("Enter ingredients separated by commas: ")
    player_ingredients = [ingredient.strip() for ingredient in player_input.split(',')]

    print("\nAI is brewing its potion...")
    time.sleep(1)  # Add a delay for suspense

    ai_ingredients = random.sample(ingredients, k=len(player_ingredients))
    ai_input = ', '.join(ai_ingredients)

    print(f"\nYou entered: {', '.join(player_ingredients)}")
    print(f"AI entered: {ai_input}")

    # Visual representation for potion race
    print("\nVisual Representation:")
    print(f"{'='*30}")
    print("     /\\_/\\                ")
    print("    ( o.o )               ")
    print("    > ^ <   ---- Potion!   ")
    print(f"{'='*30}\n")

    # Determine the winner based on the match of ingredients
    if set(player_ingredients) == set(ai_ingredients):
        print("\nCongratulations! You and the AI brewed matching potions.")
        print("You both advance in skill.")
    else:
        print("\nOops! The potions don't match. The AI gains an advantage.")

def main():
    player_skill = 0
    ai_skill = 0
    target_skill = 20

    print("\n" + "="*40)
    print(" Welcome to the Magical Potions Adventure! ")
    print("="*40 + "\n")

    while player_skill < target_skill and ai_skill < target_skill:
        print("\nOptions:")
        print("1. Brew a potion")
        print("2. Enter ingredients in a potion race")
        print("3. Check your skill level")
        print("4. Quit the game")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nBrewing a potion...")
            time.sleep(1)  # Add a delay for suspense

            # Player's turn
            player_roll = roll_dice()
            print(f"You rolled a {player_roll}")
            player_potion_quality = brew_potion(player_skill)
            print(f"You brewed a potion with a quality of {player_potion_quality}")
            player_skill += player_potion_quality

            # Random event
            if random.choice([True, False]):
                print("\nUnexpected event:")
                print(random_event())

            print(f"Your current skill level: {player_skill}")

            # AI's turn
            print("\nAI's turn...")
            time.sleep(1)  # Add a delay for suspense
            ai_roll = roll_dice()
            print(f"The AI rolled a {ai_roll}")
            ai_potion_quality = brew_potion(ai_skill)
            print(f"The AI brewed a potion with a quality of {ai_potion_quality}")
            ai_skill += ai_potion_quality

            # Random event for the AI
            if random.choice([True, False]):
                print("\nUnexpected event for the AI:")
                print(random_event())

            print(f"AI's current skill level: {ai_skill}")

        elif choice == "2":
            potion_race()

        elif choice == "3":
            print(f"\nYour current skill level: {player_skill}")
            print(f"AI's current skill level: {ai_skill}")

        elif choice == "4":
            print("\nExiting the game. Thanks for playing!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

    # Determine the winner and the ending
    if player_skill >= target_skill:
        print("\nCongratulations! You have mastered the art of potion brewing.")
        print("You have a happy ending and become a renowned potion master.")
    else:
        print("\nOops! The AI has outperformed you in potion brewing.")
        print("The AI has a happy ending and becomes a legendary potion master.")

if __name__ == "__main__":
    main()
