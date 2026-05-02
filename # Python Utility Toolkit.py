# Python Utility Toolkit

# 1. Polynomial evaluation

def poly_eva():
    exp = {
        2: 2,
        1: 3,
        0: 5
    }

    x = int(input("Define value of x: "))
    total = 0

    for power, coeff in exp.items():
        print("power: ,", power, "coefficient: ", coeff)
        total += coeff * (x**power)

    print("Total: ", total)


# 2. Multiples within a range

def multi_range():
    a= int(input("Whose multiples do you need? "))
    b= int(input("From: "))
    c= int(input("To: "))

    # exception handling
    if b > c:
        b, c = c, b

    #actual loop
    for x in range(b, c+1):
        print(x, "into", a, "is: ",x*a)

# 3. Greatest of three numbers

def greatest_of_three():
    a = int(input('First No.= '))
    b = int(input('Second No.= '))
    c = int(input('Third No.= '))
    
    if (a>b and a>c):
        print ("First No. is greatest")

    elif b>a and b>c:
        print ("Second No. is the greatest")

    else:
        print ("Third No. is the greatest")





