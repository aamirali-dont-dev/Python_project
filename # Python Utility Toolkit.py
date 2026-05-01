# Python Utility Toolkit

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






