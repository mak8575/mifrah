'''
def countdown(number):
    total = 0
    while number>=0:
        print(number)
        total += number
        number -= 1
    return total
def main():
    num = int(input("Enter a number:"))
    resultdown = countdown(num)
    print("the sum is:", resultdown)
main()
'''


def countdown(number):
    total =0
    while number>=0:
        total = total + number
        print(number)
        number -=1
    return total
    print(total)
countdown(8)








