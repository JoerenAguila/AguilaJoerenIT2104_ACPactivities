def is_palindrome(number):
    str_num = str(number)
    if str_num == str_num[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")
num = int(input("Enter an integer: "))
is_palindrome(num)
