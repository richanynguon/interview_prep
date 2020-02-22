from performance_tester import performance_tester

#o(n)
def max_char(word):
    count = {}
    highest_value = ""
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
        if highest_value is '':
            highest_value = char
        else:
            if count[char] > count[highest_value]:
                highest_value = char
    return highest_value

#o(n) - slightly faster
def max_char_second(word):
    return max(word, key=word.count)


performance_tester([max_char, max_char_second], ["ifeel", "firewhenthe", "imstilltryingtofigureout",
                                "starringataccrosstheroombetimatrendsettertoowoahhohoh"], ylim=False)
