palindromes = []
words = ["makikaki","kerekes","kakóbab","kutatás","lehetőség","programozott","fafaragás"]
palindromes_set = set()

def create_palindrome(word):
    word = word.upper()
    l = len(word) -1
    drow = ""
    while l >= 0:
        drow += word[l]
        l -= 1
    return word + drow

def create_mirror(word):
    word = word.upper()
    l = len(word) -1
    drow = ""
    while l >= 0:
        drow += word[l]
        l -= 1
    return drow

def search_palindrome(word):
    word = word.upper()
    if word == create_mirror(word):
        palindromes.append(word)
    return palindromes

def search_inword_palindrome_list(word):

    word = word.upper()
    l = len(word)

    for i in range(l):
        for j in range(0, i):
            chunk = word[j:i + 1]

            if chunk == chunk[::-1]:
                if len(chunk) > 2:
                    palindromes.append(chunk)

    return palindromes

def search_inword_palindrome_set(word):

    word = word.upper()
    l = len(word)

    for i in range(l):
        for j in range(0, i):
            chunk = word[j:i + 1]

            if chunk == chunk[::-1]:
                if len(chunk) > 2:
                    palindromes_set.add(chunk)

    return palindromes_set

def search_palindromes_inlist(words_list):
    palindromes_set.clear()
    for word in words_list:
        search_inword_palindrome_set(word)
    return palindromes_set

print(create_palindrome("macska"))
print(search_palindrome("gereg"))
print(search_inword_palindrome_list("kutató"))
print(search_inword_palindrome_set("ratatata"))
print(search_palindromes_inlist(words))
