from performance_tester import performance_tester

def palindrome(word):
  reverse = word[::1]
  if reverse == word:
    return True
  else:
    return False

print(palindrome("forgeeksskeegfor"))
print(performance_tester([palindrome], ["kayak", "forgeeksskeegfor", "qweqwewqewqewqewqewqewqeqweqweqweqweqweqwewqewq", "qweqwewqewqewqewqewqewqewqesseeeghjetwrtwetsdhrirhdstewtrwtejhgeeesseqweqweqweqweqweqweqwewqewq", "imreallytryingtomakeawordthatscalesandkindofshowswhatneedstobeseenreallythoughimjusttryingtomakethisworkdkrowsihtekamotgniyrttsujmihguohtyllaerneesebotsdeentahwswohsfodnikdnaselacstahtdrowaekamotgniyrtyllaermi"], 1000000))