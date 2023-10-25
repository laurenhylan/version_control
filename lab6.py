# Lauren Hylan
# define encode program
def input_encode(encode_input):
    password_encoded = ''
    for digit in encode_input:
        input_digit = int(digit)

        if input_digit == 7:   # the value 7 (+3), outputs 0
            encode_digit = 0
            password_encoded += str(encode_digit)
        elif input_digit == 8:   # the value 8 (+3), outputs 1
            encode_digit = 1
            password_encoded += str(encode_digit)
        elif input_digit == 9:   # the value 9 (+3), outputs 2
            encode_digit = 2
            password_encoded += str(encode_digit)
        else:
            encode_digit = input_digit   # else, value (+3)
            encode_digit += 3
            password_encoded = str(encode_digit)
    return password_encoded


if __name__ == '__main__':   # version control menu ENCODE
    control_menu = True

    while control_menu:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            encoder = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
        elif menu_option == 2:
            encoded_password = input_encode(encoder)
            print(f'The encoded password is {encoded_password}, and the original password is {encoder}.')
        elif menu_option == 3:
            control_menu = False
