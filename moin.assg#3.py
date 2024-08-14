import hashlib  # provides a helper function for efficient hashing of a file.
import secrets  # secrets module is used for generating random numbers.

with open("user_pass_1.txt", "a") as file: #Creating a file which stores user names, passwords, Hashes, and salt
    
    file.write("USERNAME\tPASSWORD\tSALT\tHASH\n")

while True: 
    print("1. Sign up: ")
    print("2. Sign in: ")
    print("3. Exit: ")
    option = input("Select an Option: ")
    
    if option == '1':
        # Signing up for creation of account.
        print("No account? Create one!")
        user_input_name = input("Enter the Username: ")
        user_input_pass = input("Enter a Password: ")
        
        salt = secrets.token_hex(16)
        combined = user_input_pass + salt
        pass_hash = hashlib.sha256(combined.encode()).hexdigest()
        
        # Open the file to add new user data
        with open("user_pass_1.txt", "a") as file:
            formatted_data = f"{user_input_name}\t{user_input_pass}\t{salt}\t{pass_hash}\n"
            file.write(formatted_data)
        print("Account Created successfuly!")
        
    elif option == '2':
        # Signing in to your account.
        
        username_to_check = input("Enter the Username: ")
        print("Forgot Password?")
        password_to_check = input("Enter a Password: ")
        
        
        with open("user_pass_1.txt", "r") as file:
            for line in file:
                data = line.strip().split('\t')
                username, password, salt, hash = data
                if username == username_to_check:
                    combined = password_to_check + salt
                    input_hash = hashlib.sha256(combined.encode()).hexdigest()
                    if input_hash == hash:
                        print("You are now logged in!")
                        break
            else:
                print("The user name or password you entered is incorrect.")
                
    elif option == '3':
        break
    else:
        print("Invalid choice. Please try again.")
      
      #When creating a new account, if incase the passwords of two accounts by chance the same, it will generate different hashes.
      #It is because we use salt technique which differ the same password with different hashes. H(P+S)
      