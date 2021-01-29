def hello():
    print("ECSE3038 - Engineering IoT Systems")

hello()

def validatePassword(password):

    numCount = 0;

    if len(password) > 7 and password.isalnum():
        
        for character in password:

            if character.isnumeric():
                numCount += 1
        
        return True if numCount >= 2 else False

    else:
        return False


password = input("Please enter your password: ")

print(validatePassword(password))


