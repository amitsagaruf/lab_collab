# Amit Sagar
def encode(password):
    encoded_password = ''
    print("Your password has been encoded and stored!\n")
    for num in password:
        if int(num) >= 7:
            num = int(num) - 7
            encoded_password += str(num)
        else:
            encoded_password += str(int(num) + 3)
    return encoded_password



def decode(password):  # decodes password by subtracting 3 from each number in password (Made by: Zachary Bradley)
        dec_pass = ''
        password = str(password)
        for digit in password:
            dec_pass += str(int(digit) - 3) if int(digit) >= 3 else str(int(digit) + 7)
        return int(dec_pass)


def main():
    option = None
    encoded_password = None
    decoded_password = None
    while option != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            encoded_password = encode(input("Please enter your password to encode: "))
        if option == 2:
            print(f"The encoded password is {encoded_password}, and the original"
                  f" password is {decode(encoded_password)}.\n")
        if option == 3:
            break


if __name__ == '__main__':
    main()
