import logging

# Configure logging to file
logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception
class InvalidInputError(Exception):
    pass


def get_number():
    user_input = input("Enter a positive integer (or 'q' to quit): ")

    if user_input.lower() == "q":
        raise SystemExit

    if not user_input.isdigit():
        raise InvalidInputError(f"Invalid input: '{user_input}' is not a positive integer")

    return int(user_input)


# Main loop
while True:
    try:
        num = get_number()
        print(f"You entered: {num}")

    except InvalidInputError as e:
        print("Please enter a valid positive integer!")
        logging.error(e)   # log the error

    except Exception as e:
        print("Unexpected error occurred. Exiting...")
        logging.exception(e)
        break
