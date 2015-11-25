import db

datas = db.data()
weeks = len(datas)
numbers = []
numbers_dictionary = {}

def makePulledNumbersList():
    i = 0
    while i < weeks:
        n = 11
        while n < 16:
            pulled_number = datas[i] [n]
            numbers.append(pulled_number)
            n += 1
        i += 1

def makeTheDictionary():
    for x in numbers:
        if x not in numbers_dictionary.keys():
            numbers_dictionary[x] = 1
        else:
            numbers_dictionary[x] += 1

def listTopFive():
    topFive = [(v, k) for k, v in numbers_dictionary.items()]
    topFive.sort()
    topFive.reverse()
    topFive = [(k, v) for v, k in topFive]
    topFive = topFive[0:5]
    print("A leggyakrabban kihúzott 5 szám , hányszor húzták ki: ")
    for i in topFive:
        num, summa = i
        print(num, "," ,summa)

makePulledNumbersList()
makeTheDictionary()
listTopFive()
