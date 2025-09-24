number = int(input("Enter a number:"))


def even_or_odd():
    """
    Creating a fun
def square():
    return number**2

def cube_of_number():
    return number ** 3ction to see if the number given by the user if even or odd.
    """
    if number%2==0:
        return "even"
    else:
        return "odd"

def pos_or_neg():
    """
    To check if the number given by the user is positive or negative.
    """
    if number > 0:
        return "Positive"
    else:
        return "Negative"


def main():
    result1 = even_or_odd()
    result2 = pos_or_neg()
    result3 = square()
    result4 = cube_of_number()
    print("The number is:", result1)
    print("The number is:", result2)
    print("The square of the number is: ", result3)
    print("The cube of the number is:",result4)
main()