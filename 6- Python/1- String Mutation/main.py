def string_modification(string_input, position, new_string):
    """
    This function modifies a value in a string based on a certain index.

    :param string_input: String to be modified.
    :param position: Index to the target position.
    :param new_string: String to replace old value.

    :return final_string: Modified string.
    """
    string_list = list(string_input)
    string_list[position] = new_string
    final_string = ''.join(string_list)
    return final_string


string_to_modify = ''

while True:
    try:
        print('*' * 70)

        # Get string input from user or exit program
        string_to_modify = input("Enter a string or exit program: ")
        if string_to_modify == "exit":
            break
        print("Original string: ", string_to_modify)

        # Ask user for index
        index_to_modify = int(input("Enter the index that you want to replace its value: "))

        # Handle out of range errors immediately
        if index_to_modify >= len(string_to_modify) or index_to_modify < -len(string_to_modify):
            raise IndexError

        # Ask user for new value
        new_value = input("Enter the new value: ")

        # Replace old value with new one and print result
        modified_string = string_modification(string_to_modify, index_to_modify, new_value)
        print("\nThe modified string is:", modified_string)

    # Handling wrong index types
    except ValueError:
        print("\nInvalid index!, please enter an integer.")

    # Handling out of range index
    except IndexError:
        print(f"\nThe index you entered is out of range.\n"
              f"Your range is: [0 to {len(string_to_modify)-1}] "
              f"or [-{len(string_to_modify)} to -1]")

    # Exit program guidance
    print("\nLet's try again! you can type exit when you're done.")

print("\nThank you! and I hope you a wonderful day.\n")
