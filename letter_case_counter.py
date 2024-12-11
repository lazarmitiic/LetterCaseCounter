def count_uppercase_letters(text):
    """Counts and displays the number of uppercase letters in the text."""
    uppercase_letters = [char for char in text if char.isupper()]
    if uppercase_letters:
        print(f"Number of uppercase letters: {len(uppercase_letters)}")
    else:
        print("Your text has no uppercase letters.")

def count_lowercase_letters(text):
    """Counts and displays the number of lowercase letters in the text."""
    lowercase_letters = [char for char in text if char.islower()]
    if lowercase_letters:
        print(f"Number of lowercase letters: {len(lowercase_letters)}")
    else:
        print("Your text has no lowercase letters.")

def count_digits(text):
    """Counts and displays the number of digits in the text."""
    digits = [char for char in text if char.isdigit()]
    if digits:
        print(f"Number of digits: {len(digits)}")
    else:
        print("Your text has no digits.")

def count_special_characters(text):
    """Counts and displays the number of special characters in the text."""
    special_characters = [char for char in text if not char.isalnum()]
    if special_characters:
        print(f"Number of special characters: {len(special_characters)}")
    else:
        print("Your text has no special characters.")

def main():
    """Main function to take user input and count letter cases, digits, and special characters."""
    text = input("Input some text: ")
    count_uppercase_letters(text)
    count_lowercase_letters(text)
    count_digits(text)
    count_special_characters(text)

if __name__ == "__main__":
    main()
