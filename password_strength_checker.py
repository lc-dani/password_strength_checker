# Make criteria for strong password
# - At least 20 characters long
# - The full password cannot be a word out of the dictionary
# - Should not exist out of repeating characters
# - Exists out of randomized characters
# - Includes special characters, numbers and capital letters 


def test_password_strength():
    special_char_count = 0
    capital_char_count = 0
    given_password = input("Fill in your password: ")

    if len(given_password) < 20 and len(set(given_password)) != len(given_password):
        print("\n- Invalid password! Password contains repeating characters and is too short.")
    elif len(given_password) < 20:
        print("\n- Invalid password! Password is too short.")
    elif len(set(given_password)) != len(given_password):
        print("\n- Invalid password! It contains repeating characters.")
    
    special_character = '!@#$%&*()_:,./<>?[]'
    
    for character in range(len(given_password)):
        if given_password[character] in special_character:
            special_character += 1

    if special_char_count == 0:
        print("\n- Invalid password! does not contain special characters.")

    for character in range(len(given_password)):
        if given_password[character].isupper():
            capital_char_count += 1

    if capital_char_count == 0:
        print("\n- Invalid password! It does not contain a capital letter.")

if __name__ == "__main__":
    test_password_strength()