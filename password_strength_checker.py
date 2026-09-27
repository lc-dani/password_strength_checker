# Make criteria for strong password
# - At least 20 characters long
# - The full password cannot be a word out of the dictionary
# - Should not exist out of repeating characters
# - Exists out of randomized characters
# - Includes special characters, numbers and capital letters 


def test_password_strength():
    given_password = input("Fill in your password: ")

    if len(given_password) < 20:
        print("\nInvalid password, too short!")

    if len(set(given_password)) != len(given_password):
        print("\nInvalid password, contains repeating characters!")

    special_character = '!@#$%&*()_:,./<>?[]'

    special_char_count = 0
    
    for character in range(len(given_password)):
        if given_password[character] in special_character:
            special_character += 1

    if special_char_count == 0:
        print("\nInvalid password, does not contain special characters!")


if __name__ == "__main__":
    test_password_strength()