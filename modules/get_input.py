"""
Functions for checking and processing user input.

Currently contains a single function, but more can be added to meet future user input requirements.
"""

def integer(message, min, max, default):
    """ 
    Takes user input as user_input and converts to an integer if possible.
    Minimum and maximum values are passed to the function to restrict the range of the input.
    Function is recursive when non-numeric characters are entered.

    Args:

        message:
            A string requesting user input.

        min:
            The minimum permitted value.

        max:
            The maximum permitted value.

        default:
            A default value, used if user_input is empty.

    Returns:

        num:
            An integer specified by the user (if user_input is valid).

        default:
            A default integer (if user_input is empty).

    """
    user_input = input(message)
    if user_input:
        try:
            num = int(user_input)
            if num < min or num > max:
                print(f"Error. Please enter a value between {min} and {max}.")
                return integer(message, min, max, default)  # Invalid input leads to recursive function call.
            return num
        except ValueError:
            print("Error. Non-numeric character(s) entered. Please enter numeric characters only.")
            return integer(message, min, max, default)  # Invalid input leads to recursive function call.
    else:
        return default