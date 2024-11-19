def is_perfect_number(number):
    if number < 1:
        return False
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

def main():
    while True:
        user_input = input("Enter a number: ").strip()
        if not user_input.isdigit():
            print("Please enter a valid integer.")
            continue
        
        number = int(user_input)
        if is_perfect_number(number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
        
        break  
if __name__ == "__main__":
    main()
