import random
import string


def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    char_sets = []
    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
    if use_numbers:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("Select at least one character type.")

    password = []
    for charset in char_sets:
        password.append(random.choice(charset))

    remaining_length = length - len(password)
    all_characters = "".join(char_sets)
    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return "".join(password)


def main():
    print("Password Generator")
    print("=================")

    while True:
        try:
            length = int(input("Enter desired password length: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() != "n"
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() != "n"
    use_numbers = input("Include numbers? (y/n): ").strip().lower() != "n"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() != "n"

    try:
        password = generate_password(
            length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_numbers=use_numbers,
            use_symbols=use_symbols,
        )
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print("Generated password:")
    print(password)


if __name__ == "__main__":
    main()
