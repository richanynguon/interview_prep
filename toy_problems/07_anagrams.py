from performance_tester import performance_tester
# should build in edge cases for capital letters and what not
# o(N)


def anagrams(first, second):
    char_map = {}
    if len(first) is not len(second):
        return False
    else:
        for char in first:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        for char in second:
            if char in char_map:
                if char_map[char] > 0:
                    char_map[char] -= 1
                else:
                    return False
            else:
                return False
        return sum(char_map.values()) is 0

# o(n) but slightly faster


def anagrams_sorted(first, second):
    first_word = sorted(list(first))
    second_word = sorted(list(second))
    string_first = ''
    string_first = string_first.join(first_word)
    string_second = ''
    string_second = string_second.join(second_word)
    return string_second == string_first

# o(n)
def anagrams_replace(first, second):
    second_word = second
    for char in first:
        if char in second:
            second_word = second_word.replace(char, "0", 1)
        else:
            return False
    if (len(second)*"0") == second_word:
      return True
    else: 
      return False



performance_tester([anagrams, anagrams_sorted, anagrams_replace], [["slapslap", "plasplas"], [
                   "slapslap", "plasplass"], ["rarararararara", "ararararararar"], ["iamthesamelengthiamthesamelengthiamthesamelengthiamthesamelengthiamthesamelengthiamthesamelengthiamthesamelength", "iamthesamelengthiamthesamelengthiamthesamelengthiamthesamelengthiamthesamelengthiamthesamelengthiamthesamelength"]], multiple_inputs=True)
