#!/bin/python3

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift=None):
    if shift is not None:
        return encrypt(text, -shift)
    else:
        print("Trying all possible shifts...")
        for s in range(26):
            print(f"Shift {s}: {encrypt(text, -s)}")
        user_input = input("Enter the correct decrypted text from the above options: ")
        return user_input

def to_ascii(text):
    return [ord(char) for char in text]

def menu():
    while True:
        print("\nMenu:")
        print("1. Encrypt text")
        print("2. Decrypt text (with shift)")
        print("3. Decrypt text (without knowing shift)")
        print("4. Convert text to ASCII values")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted: {encrypted_text}")

        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted: {decrypted_text}")

        elif choice == '3':
            text = input("Enter the text to decrypt: ")
            decrypted_text = decrypt(text)
            print(f"Decrypted with correct text: {decrypted_text}")

        elif choice == '4':
            text = input("Enter the text to convert to ASCII values: ")
            ascii_values = to_ascii(text)
            print(f"ASCII Values: {ascii_values}")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
