import random

def create_passwords(lengths):
    chars = "abcdefghijklmnopqrstuvwxyz"
    results = []

    for length in lengths:
        pw = ""
        for _ in range(length):
            idx = random.randint(0, len(chars) - 1)
            pw += chars[idx]
        
        pw = insert_number(pw)
        pw = insert_uppercase(pw)
        
        results.append(pw)
    
    return results

def insert_number(password):
    for _ in range(random.randint(1, 2)):
        pos = random.randint(0, len(password) // 2 - 1)
        password = password[:pos] + str(random.randint(0, 9)) + password[pos + 1:]
    return password

def insert_uppercase(password):
    for _ in range(random.randint(1, 2)):
        pos = random.randint(len(password) // 2, len(password) - 1)
        password = password[:pos] + password[pos].upper() + password[pos + 1:]
    return password

def main():
    num_pwds = int(input("Enter the number of passwords to generate: "))
    
    print(f"Generating {num_pwds} passwords")
    
    min_length = 3
    print(f"Password length must be at least {min_length}")
    
    lengths = []
    for i in range(num_pwds):
        length = int(input(f"Enter length for Password #{i + 1}: "))
        if length < min_length:
            length = min_length
        lengths.append(length)
    
    passwords = create_passwords(lengths)
    
    for i, pwd in enumerate(passwords):
        print(f"Password #{i + 1} = {pwd}")

if __name__ == "__main__":
    main()
