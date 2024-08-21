num_multiples = 10

for i in range(1, num_multiples + 1):
    multiple_of_7 = i * 7
    
    if i % 2 == 0:
        print("\t" + str(multiple_of_7))
    else:
        print(multiple_of_7)
