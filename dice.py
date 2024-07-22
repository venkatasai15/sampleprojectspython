import random

def roll_dice(num_dice, num_sides):
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        results.append(roll)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    print("--------------------------------------")
    
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            num_sides = int(input("Enter the number of sides on each die: "))
            
            if num_dice <= 0 or num_sides <= 0:
                print("Please enter positive numbers greater than zero.")
                continue
            
            rolls = roll_dice(num_dice, num_sides)
            
            print(f"\nResults of rolling {num_dice} dice with {num_sides} sides each:")
            print(rolls)
            
            choice = input("\nDo you want to roll again? (yes/no): ").lower()
            if choice != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
