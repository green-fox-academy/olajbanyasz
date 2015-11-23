romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))

def terminate():
    terminate = input("Want more conversion Y on N :").upper()
    if terminate == "Y":
        toRoman()
    else:
        exit()

def toRoman():
    n = int(input("Write a number under 4000: "))
    if not (0 < n < 4000):
        print("number out of range, it must be 1..3999")
        terminate()

    x = 5
    romannumeral = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            romannumeral += numeral
            n -= integer
    print(romannumeral)
    terminate()

toRoman()
