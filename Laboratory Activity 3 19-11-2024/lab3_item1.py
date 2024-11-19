# lab3_item1.py

def roman_to_integer(roman):
    # Define the mapping of Roman numerals to integers
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    # Convert the input to uppercase to handle lowercase inputs
    roman = roman.upper()
    
    # Initialize variables
    total = 0
    prev_value = 0
    
    # Process the Roman numeral from right to left
    for char in reversed(roman):
        if char not in roman_values:
            # Handle invalid characters
            print(f"Invalid Roman numeral: {roman}")
            return None
        
        current_value = roman_values[char]
        
        if current_value < prev_value:
            # If a smaller numeral precedes a larger numeral, subtract
            total -= current_value
        else:
            # Otherwise, add
            total += current_value
        
        prev_value = current_value
    
    return total

# Main program
if __name__ == "__main__":
    roman_input = input("Enter a Roman numeral: ").strip()
    integer_value = roman_to_integer(roman_input)
    
    if integer_value is not None:
        print(f"The integer value of '{roman_input.upper()}' is: {integer_value}")
