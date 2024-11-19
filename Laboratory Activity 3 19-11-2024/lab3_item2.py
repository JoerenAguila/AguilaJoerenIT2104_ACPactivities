# perfect_number_checker.py

def is_perfect_number(number):
    """
    Function to check if a number is a perfect number.
    A perfect number is equal to the sum of its proper divisors (excluding itself).
    """
    if number < 1:
        return False
    
    # Find divisors and sum them up
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

def main():
    while True:
        # Prompt the user for input
        user_input = input("Enter a number: ").strip()
        
        # Validate if the input is an integer
        if not user_input.isdigit():
            print("Please enter a valid integer.")
            continue
        
        number = int(user_input)
        
        # Check if the number is perfect and display the result
        if is_perfect_number(number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
        
        break  # Exit the loop after a valid input

if __name__ == "__main__":
    main()
