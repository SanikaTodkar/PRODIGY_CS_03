import string

def score_password(password):
    """
    Calculate the strength score of a given password based on various criteria.
    """
    score = 0
    if len(password) < 8:
        return score

    score += 1
    if len(password) >= 12:
        score += 1

        if any(char.islower() for char in password):
            score += 1
        if any(char.isupper() for char in password):
            score += 1
        if any(char.isdigit() for char in password):
            score += 1
        if any(char in string.punctuation for char in password):
            score += 1

            if len(password) >= 16:
                score += 2
            if len(password) >= 24:
                score += 3

    if (any(char.islower() for char in password) and
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in string.punctuation for char in password)):
        score += 4

    return score

def main():
    """
    The main function to handle user input and display password strength.
    """
    print("Welcome to the Password Strength Assessment Tool!")
    password = input("Enter your Password: ")

    strength = score_password(password)
    if strength == 0:
        print("Very weak password. Please improve it.")
    elif strength == 1:
        print("Weak Password. Consider adding more characters.")
    elif strength == 2:
        print("Moderate Password. You can improve it further.")
    elif strength == 3:
        print("Strong password. Keep it up.")
    elif strength >= 4:
        print("Very strong password. Excellent Job!")

if __name__ == "__main__":
    main()