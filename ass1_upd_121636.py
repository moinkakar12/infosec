print('1. Encryption: \n2. Decryption: ')
option = int(input("Select An Option: "))
while True:
    msg = input("Enter Your Message = ")
    if msg.isalpha():
        break
    else:
        print("Invalid Input. Enter only Alphabets")
key = int(input("Select your Key : "))
encoded_msg = ""

# Using Nested Loop for Encryption & Decryption
if option == 1:
    for i in msg:
        if i.isalpha():  # Check if the character is an alphabet
            ascode = ord(i) + key
            if i.isupper():  # Check if the character is uppercase
                encoded_char = chr((ascode - 65) % 26 + 65)
            else:
                encoded_char = chr((ascode - 97) % 26 + 97)
            encoded_msg = encoded_msg + encoded_char
        else:
            encoded_msg = encoded_msg + i  # Keep non-alphabetic characters unchanged
    print(encoded_msg)
elif option == 2:
    for i in msg:
        if i.isalpha():
            ascode = ord(i) - key
            if i.isupper():
                encoded_char = chr((ascode - 65) % 26 + 65)
            else:
                encoded_char = chr((ascode - 97) % 26 + 97)
            encoded_msg = encoded_msg + encoded_char
        else:
            encoded_msg = encoded_msg + i
    print(encoded_msg)