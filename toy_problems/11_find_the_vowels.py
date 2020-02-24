
from performance_tester import performance_tester
#o(n) don't forget that letters have ascii that can be used
def find_vowels(word):
    counter = 0
    for char in word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            counter += 1
    return counter


performance_tester([find_vowels],["qwe","qwertyu","qwertyuiopasdfghjklzxcvbnm"])