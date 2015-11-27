words = []
palindromes_set = set()
chunk_length = 3

def filereader():
    try:
        v = open('text.txt', 'r', encoding='utf8')
    except IOError:
        print("Something went wrong with the file sorry.")
    else:
        text = set(v.read().split())
        return list(text)

filereader()

def input_chunk_length():
    try:
        chunk_length = int(input("Shortest palindrome for searh: "))
        if 2 < chunk_length  < 10:
            return chunk_length
        else:
            print("Wrong length value added, length = 3!")
            return 3
    except:
        print("Wrong length value added,  length = 3!")
        return 3

def search_inword_palindrome_set(word):

    word = word.upper()
    l = len(word)
    for i in range(l):
        for j in range(0, i):
            chunk = word[j:i + 1]

            if chunk == chunk[::-1]:
                if len(chunk) >= chunk_length:
                    palindromes_set.add(chunk)

    return palindromes_set

def search_palindromes_inlist(words_list):
    palindromes_set.clear()
    for word in words_list:
        search_inword_palindrome_set(word)
    return palindromes_set



chunk_length = input_chunk_length()
palindromes_set = search_palindromes_inlist(filereader())
if len(palindromes_set) == 0:
    print("There is no " + str(chunk_length) + " characters long or longer palindrome in the text!")
for i in palindromes_set:
    print(i)
