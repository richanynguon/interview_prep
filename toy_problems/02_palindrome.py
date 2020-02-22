from performance_tester import performance_tester


def palindrome(word):
    return word[::1] == word


def palindrome_loop(word):
    flag = True
    for i, char in enumerate(word):
        if char != word[len(word)-i-1]:
            flag = False
    return flag


print(performance_tester([palindrome, palindrome_loop], ["kayak", "forgeeksskeegfor", "qweqwewqewqewqewqewqewqeqweqweqweqweqweqwewqewq", "qweqwewqewqewqewqewqewqewqesseeeghjetwrtwetsdhrirhdstewtrwtejhgeeesseqweqweqweqweqweqweqwewqewq",
                                        "imreallytryingtomakeawordthatscalesandkindofshowswhatneedstobeseenreallythoughimjusttryingtomakethisworkdkrowsihtekamotgniyrttsujmihguohtyllaerneesebotsdeentahwswohsfodnikdnaselacstahtdrowaekamotgniyrtyllaermi"], 1000000))
