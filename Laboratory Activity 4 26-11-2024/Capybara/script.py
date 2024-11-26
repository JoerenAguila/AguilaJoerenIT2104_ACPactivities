from capybara import Capybara

capybara1 = Capybara("Biscoff", "M", 5)

capybaras = [capybara1]

test_case_number = int(input("Enter the test case number: "))

if 1 <= test_case_number <= len(capybaras):
    selected_capybara = capybaras[test_case_number - 1]
    print(f"Test Case {test_case_number}: Name: {selected_capybara.name}, "
          f"Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")
else:
    print("Invalid test case number. Please try again.")
