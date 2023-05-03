def is_leap(year):
    """
    This function takes a year as input and returns True if it is a leap year, and False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


while True:
    try:
        year = int(input("Please enter a year or exit program: "))

        # Exit program
        if year == 0:
            break

        # Handling 0's and -ve input
        if year < 0:
            raise ValueError

        # Call the is_leap function and print the result
        if is_leap(year):
            print(year, "is a leap year. Type 0 if you want to exit\n")
        else:
            print(year, "is not a leap year. Type 0 if you want to exit\n")

    # Handling user input errors
    except ValueError:
        print("Error: Please enter a valid positive integer.\n")
       
print("Program ended. Thank you!")
