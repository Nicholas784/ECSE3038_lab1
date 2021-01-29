def hello():
    print("ECSE3038 - Engineering IoT Systems")


def validatePassword(password):

    numCount = 0;

    if len(password) > 7 and password.isalnum():
        
        for character in password:

            if character.isnumeric():
                numCount += 1
        
        return True if numCount >= 2 else False

    else:
        return False


def sumUpToN(number):

    sum = 0

    if number > 0:

        for num in range(number):

            sum += num +1 
    
        return sum

    else: 
        return -1


hello()

password = input("Please enter your password: ")

print(validatePassword(password))

number = input("Please enter a number: ")

print(sumUpToN(int(number)))