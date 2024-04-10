def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == '2':
            if 'encoded_password' in locals():
                print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
            else:
                print("No password encoded yet.")
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose again.")

# Encoder function
