
def guessNumber(startRange, endRange):
    if startRange> endRange:
        return True
    
    #  find midRange
    mid = (startRange + endRange) // 2

    # Asking user about gussed num
    print(f"Is the number {mid}? (Y/N): ", end="")
    user = input().strip()
    
    #Gussed correctly
    if user in ("Y", "y"):
        print("Congrats!!!")
        return False
    
    # Gussed is incorrectly
    elif user in ("N", "n"):
        print(f"Is the actual greater no than {mid}? (Y/N): ", end="")
        user = input().strip()

        if user in ("Y", "y"):
            guessNumber(mid+1, endRange)

        elif user in ("N", "n"):
            guessNumber(startRange, mid+1)

        else:
            print("Invalid, Please Enter 'Y', 'N'.")
            return guessNumber(startRange, endRange)



# Drive Code
if __name__ == "__main__":
    print("Number Guessing Game in Python")

    #Taking input from user
    startRange = int(input("Enter starting Range: "))
    endRange = int(input("Enter End Range: "))

    print(f"Think of a number between {startRange} and {endRange} - ")

    out = guessNumber(startRange, endRange)

    if out:
        print("Couldn't guess it.")

