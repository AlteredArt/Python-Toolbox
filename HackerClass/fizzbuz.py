
choice = int(input("What number would you like to count up to?"))

def fizzbuz(choice):
    for num in range(1,choice):
        if num % 3 == 0 and num %5 ==0:
            print("fizbbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
    
print("About to run the program")

fizzbuz(choice)