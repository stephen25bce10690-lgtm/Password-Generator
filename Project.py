import random
import string

def generate_secure_password():
    """
    Generates a secure, random password based on user specifications.
    """
    print("--- Simple Password Generator ---")
    
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 12): "))
            if length <= 0:
                print("Length must be a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    char_sets = {
        'letters': string.ascii_letters,
        'numbers': string.digits,
        'symbols': string.punctuation
    }
    
    use_letters = input("Include letters (y/n)? ").lower() == 'y'
    use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

    if not (use_letters or use_numbers or use_symbols):
        print("\nError: You must select at least one character type.")
        return

    character_pool = ""
    guaranteed_chars = []
    
    if use_letters:
        character_pool += char_sets['letters']
        guaranteed_chars.append(random.choice(char_sets['letters']))
    if use_numbers:
        character_pool += char_sets['numbers']
        guaranteed_chars.append(random.choice(char_sets['numbers']))
    if use_symbols:
        character_pool += char_sets['symbols']
        guaranteed_chars.append(random.choice(char_sets['symbols']))
        
    remaining_length = length - len(guaranteed_chars)
    
    if remaining_length < 0:
   
        print(f"\nWarning: Password length adjusted to {len(guaranteed_chars)} to include all selected character types.")
        remaining_length = 0

    random_filler = [random.choice(character_pool) for _ in range(remaining_length)]
    
    password_list = guaranteed_chars + random_filler
    random.shuffle(password_list)
    
    final_password = "".join(password_list)

    print(f"\nGenerated Password: **{final_password}**")
    print(f"Length: {len(final_password)}")

if __name__ == "__main__":
    generate_secure_password()
