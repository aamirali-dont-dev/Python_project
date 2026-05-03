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

# 10.a Decimal to Binary
def dec_bin():
    bin = []
    n = int(input("Enter a decimal number: "))
    
    while n > 0:
        r = n % 2
        bin.append(r)
        n = n // 2
    bin.reverse()
    print(bin)

# 10.b Binary to Decimal
def bin_dec():
    bin = input("Enter a binary number: ")

    i = len(str(bin)) - 1
    ans = int()

    while bin >= 0:
        q = bin % i
        ans += q * 2 ** i
        bin = bin // 10
        i -= 1
    print(ans)

# 11. Prime Numbers in a Range
def prime_range():
    a = int(input("From: "))
    b = int(input("To: "))

    for num in range(a, b+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, "is a prime number")

# 12. Number Name
def num_name():

    names = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    n = int(input("Enter a number: "))
    ans = []

    for digit in n:
        ans.append(names[int(digit)])

    print(" ".join(ans))
num_name()

# INCOMPLETED

# 13. Smallest in an Array
def smallest_in_array():
    newar = [int(x) for x in input("Enter numbers in the array: ").split()]
    smallest = newar[0]

    for i in newar:
        if i < smallest:
            smallest = i

    print(smallest, "is the smallest number in the array")

# 14. Search a num in an Array
def search_in_array():
    newar = [int(x) for x in input("Enter numbers in the array: ").split()]
    n = int(input("Enter a number to search for: "))

    for i in newar:
        if i == n:
            print(n, "is present in the array")
            break
    else:
        print(n, "is not present in the array")

# 15. Factorial of a number
def factorial():
    n = int(input("Enter a number: "))
    fact = 1

    for i in range(1, n+1):
        fact *= i

    print(fact, "is the factorial of ", n)

# 16. Currency Note Denominations
def currency_denominations():
    n = int(input("Enter an amount: "))
    notes = [5000, 1000, 500, 100, 50, 10]
    ans = []

    for note in notes:
        q = n // note
        n = n % note
        ans.append(q)

    print(ans)

# 17. Set Operations
def set_operations():
    set1 = set(input("Enter elements of set 1: ").split())
    set2 = set(input("Enter elements of set 2: ").split())

    print("Union: ", set1.union(set2))
    print("Intersection: ", set1.intersection(set2))
    print("Difference (set1 - set2): ", set1.difference(set2))
    print("Difference (set2 - set1): ", set2.difference(set1))


# 18. Student Record (Dictionary)
def student_record():
    record = {}
    n = int(input("How many students? "))

    for i in range(n):
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        record[name] = grade

    print(record)

def menu():
    print("Welcome to the Python Utility Toolkit!")
    print("1. Polynomial evaluation")
    print("2. Multiples within a range")
    print("3. Greatest of three numbers")
    print("4. Electricity Bill Calculation")
    print("5. Student Grade Calculation")
    print("6. Find all factors of a number")
    print("7. GCD & LCM")
    print("8. Even or Odd")
    print("9. Prime or Composite")
    print("10 Decimal to Binary")
    print("11 Binary to Decimal")
    print("12. Prime Numbers in a Range")
    print("13. Number Name")
    print("14. Smallest in an Array")
    print("15. Search a num in an Array")
    print("16. Factorial of a number")
    print("17. Currency Note Denominations")
    print("18. Set Operations")
    print("19. Student Record (Dictionary)")
    print("20. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            poly_eva()
        elif choice == 2:
            multi_range()
        elif choice == 3:
            greatest_of_three()
        elif choice == 4:
            bill_cal()
        elif choice == 5:
            Grade_cal()
        elif choice == 6:
            factor_finder()
        elif choice == 7:
            GCDandLCM()
        elif choice == 8:
            even_odd()
        elif choice == 9:
            primeandcomposite()
        elif choice == 10:
            dec_bin()
        elif choice == 11:
            bin_dec()
        elif choice == 12:
            prime_range()
        elif choice == 13:
            num_name()
        elif choice == 14:
            smallest_in_array()
        elif choice == 15:
            search_in_array()
        elif choice == 16:
            factorial()
        elif choice == 17:
            currency_denominations()
        elif choice == 18:
            set_operations()
        elif choice == 19:
            student_record()
        elif choice == 20:
            print("Exiting...")
            break
menu()