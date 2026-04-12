#PS 1st CP2 This is where all of the user input error handling functions go

def stupid_proofed_inputs(message,method,*allowed_inputs):
    while True:
        user_data = ""
        if method == "lower":
            user_data = input(f"\n\n{message}").strip().lower()
        elif method == "title":
            user_data = input(f"\n\n{message}").strip().title()
        elif method == "number":
            while True:
                user_data = input(f"\n\n{message}").strip()
                try:
                    float(user_data)
                    break
                except ValueError:
                    print("\n\nWrite a number")
        elif method == "none":
            user_data = input(f"\n\n{message}").strip()
        else:
            print("Programmer ERROR: used improper method")
        if user_data in allowed_inputs:
            return user_data
        if "_" in allowed_inputs:
            return user_data
        else:
            print("\n\nYou have inputed something in incorrectly please try again")


def positivity(user_input):
    if float(user_input) < 0 :
        return float(user_input)* -1
    elif float(user_input) == 0:
        return "1"
    else:
        return user_input


#decorator for loops
def decorator(func):
    def looper(*args):
        while True:
            func(*args)
            if func.__name__ == "main":
                done = stupid_proofed_inputs("Are you done using this program? (y/n) ?","lower","y","n")
            else:
                done = stupid_proofed_inputs("Are you done using this mode? (y/n) ?","lower","y","n")
            if done == "y":
                break
            elif done == "n":
                print("continue")
            else:
                print("Please only type y for yes or n for no.")
    return looper
