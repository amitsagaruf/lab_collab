# Amit Sagar
def encode(password):
    print("Your password has been encoded and stored!")
    return password + 33333333

# test change
def decode():
    pass


def main():
    option = None
    encoded_password = None
    decoded_password = None
    while option != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            encoded_password = encode(int(input("Please enter your password to encode: ")))
        if option == 2:
            pass
        if option == 3:
            break


main()
