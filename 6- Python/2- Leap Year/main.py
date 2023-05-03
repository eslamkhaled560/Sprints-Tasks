def is_leap(year):
    """
    This function takes a year as input and returns True if it is a leap year, and False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


while True:
    try:
        year = input("Please enter a year or exit program: ")

        # Exit program
        if year == "exit":
            break

        int_year = int(year)

        # Handling 0's and -ve input
        if int_year <= 0:
            raise ValueError

        # Call the is_leap function and print the result
        if is_leap(int_year):
            print(int_year, "is a leap year.")
        else:
            print(int_year, "is not a leap year.")

    # Handling user input errors
    except ValueError:
        print("Error: Please enter a valid positive integer.")

    print("You can type exit when you're done\n")
