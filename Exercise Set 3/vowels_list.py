def find_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = [char for char in input_string if char in vowels]
    return result

input_string = input("Enter a string: ")
vowels_in_string = find_vowels(input_string)
print("Vowels in the string:", vowels_in_string)
