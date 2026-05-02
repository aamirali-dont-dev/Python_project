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
        print("power: ", power, ", coefficient: ", coeff)
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

# 4. Electricity Bill Calculation
def bill_cal():
    units = int(input("Number of Units: "))
    total = 0

    if units <= 100:
        total += units*5 

    elif units <= 200:
        total += (100*5) + (units-100) * 8
    
    else:
        total += (100*5) + (100*8) + (units-200) * 10
    
    total += total * .10
    print(total)

# 5. Student Grade Calculation
def Grade_cal():
    Marks = int(input("Input Marks to assign grade to: "))

    if Marks >= 90:
        print("A")
    elif Marks >= 80:
        print("B")
    elif Marks >= 70:
        print("C")
    elif Marks < 70:
        print("Fail")

# 6. Find all factors of a number

def factor_finder():
    x = int(input("Give a number to find factors of: "))

    for i in range(1, x+1):
        if x % i == 0:
            print(i, "is a factor")

# 7. GCD & LCM

def GCDandLCM():

    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    
    v = a
    x = b

    if a < b:
        a, b = b, a

    while b != 0:

        r = a % b
    
        a, b = b, r

    print(a, "is the GCD of the two numbers")

    lcm = (v * x) // a
    print(lcm, "is the LCM of the two numbers")

# 8. Even or Odd
def even_odd():
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

# 9. Prime or Composite
def primeandcomposite():
    n = float(input("Enter a number: "))
    
    s_n = n ** 0.5
    s_n = int(s_n)
    for i in range(2, s_n):
        if n % i == 1:
            print(n, "is prime")
            break
        else:
            print(n, "is composite")
            break

# 10. Decimal to Binary, Binary to Decimal
def dec_bin():
    bin = []
    n = int(input("Enter a decimal number: "))
    
    while n > 0:
        r = n % 2
        bin.append(r)
        n = n // 2
    bin.reverse()
    print(bin)

dec_bin()

    

