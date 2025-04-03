number = input("Enter a 10-digit number: ")

if len(number) == 10 and number.isdigit():
    second_digit = int(number[1])
    eighth_digit = int(number[7])
    total = second_digit + eighth_digit
    print("The sum of the 2nd and 8th digits is:", total)
else:
    print("Please enter a valid 10-digit number.")
