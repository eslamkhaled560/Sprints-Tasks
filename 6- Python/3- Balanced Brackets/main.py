def is_balanced(brackets):
    """
    This function takes a string of brackets as an input and returns whether it's balanced or not.

    Args:
        brackets (str): The string of brackets to check.

    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    stack = []  # Initialize a stack to keep track of the opening brackets
    mapping = {')': '(', '}': '{', ']': '['}  # Define a mapping of opening to closing brackets

    # Iterate through each bracket in the input string
    for bracket in brackets:
        if bracket in mapping:  # If the current character is a closing bracket
            if not stack:  # If there are no opening brackets on the stack, the brackets are not balanced
                return False
            # Pop the top element from the stack and check if it matches the current closing bracket
            top_element = stack.pop()
            if mapping[bracket] != top_element:
                return False
        else:  # If the current character is an opening bracket, push it onto the stack
            stack.append(bracket)

    # If the stack is empty, the brackets are balanced. Otherwise, they're not balanced.
    return not stack


while True:
    str_brackets = input("Please enter the brackets string: ")
    if str_brackets == "exit":
        break

    error_list = []
    for char in str_brackets:
        if char not in ['(', ')', '[', ']', '{', '}']:
            error_list.append(1)

    if error_list:
        print("Error!")
        continue

    print("YES") if is_balanced(str_brackets) else print("NO")
