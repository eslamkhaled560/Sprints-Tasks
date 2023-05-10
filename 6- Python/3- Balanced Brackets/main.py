def is_balanced(brackets):
    """
    This function takes a string of brackets as an input and returns whether it's balanced or not.
    """
    # Initialize a list to keep track of opening brackets
    stack = []
    # Define a mapping of opening to closing brackets
    mapping = {')': '(', '}': '{', ']': '['}

    for bracket in brackets:
        # If closing bracket check
        if bracket in mapping:
            # If list is empty, the string is not balanced
            if not stack:
                return False
            else:
                # Pop the last element and check if it matches the current closing bracket
                last_element = stack.pop()
                if mapping[bracket] != last_element:
                    return False
        # If opening bracket, push it onto the list
        else:
            stack.append(bracket)

    # If the final list is empty, the brackets are balanced. Otherwise, they're not.
    return not stack


while True:
    str_brackets = input("Please enter the brackets string: ")
    # Exit program with empty input or only white spaces
    if not str_brackets or str_brackets.isspace():
        break
    # Remove white spaces in a string
    else:
        str_brackets = str_brackets.replace(" ", "")

    error_list = []
    # Limit input string to be only brackets
    for char in str_brackets:
        if char not in ['(', ')', '[', ']', '{', '}']:
            # Fill the error list with 1's for every non bracket char
            error_list.append(1)
    # If error list is not empty, print error and continue
    if error_list:
        print("Error! This program is made to check only brackets input [(, ), [, ], {, }]"
              "\nPlease don't provide any other character.\n")
        print("You can Exit program if you pressed enter without any input.\n")
        continue

    # Function call and result printing
    print("YES") if is_balanced(str_brackets) else print("NO")
    print("You can Exit program if you pressed enter without any input.\n")

print("\nProgram stopped, Have a good day!\n")
