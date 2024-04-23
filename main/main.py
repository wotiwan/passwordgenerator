import random
import string


def generate_password(length=8, use_digits=True, use_letters=True, use_symbols=True):

    if not (use_digits or use_letters or use_symbols):
        raise ValueError("At least one of use_digits, use_letters, or use_symbols must be True")

    characters = ''
    if use_digits:
        characters += string.digits
    if use_letters:
        characters += string.ascii_letters
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    use_digits = input("Use digits? (yes/no): ").lower() == 'yes'
    use_letters = input("Use letters? (yes/no): ").lower() == 'yes'
    use_symbols = input("Use symbols? (yes/no): ").lower() == 'yes'

    password = generate_password(length, use_digits, use_letters, use_symbols)
    print("Generated Password:", password)
