from performance_tester import performance_tester

# o(n)


def sentence_capitalization(sentence_string):
    words_array = sentence_string.split(" ")
    temp = []
    for word in words_array:
        if len(word) is 1:
            if word == word.upper():
                temp.append(word)
            else:
                temp.append(word.upper())
        else:
            split_word = list(word)
            if split_word[0] == split_word[0].upper():
                capitalized_word = ""
                capitalized_word = capitalized_word.join(split_word)
                temp.append(capitalized_word)
            else:
                split_word[0] = split_word[0].upper()
                capitalized_word = ""
                capitalized_word = capitalized_word.join(split_word)
                temp.append(capitalized_word)
    new_sentence = " "
    new_sentence = new_sentence.join(temp)
    return new_sentence

# o(n)


def sentence_capitalization_slice(sentence_string):
    words_array = sentence_string.split(" ")
    temp = []
    for word in words_array:
        if len(word) is 1:
            if word == word.upper():
                temp.append(word)
            else:
                temp.append(word.upper())
        else:
            split_word = list(word)
            if split_word[0] == split_word[0].upper():
                temp.append(word)
            else:
                capitalized_word = split_word[0].upper()+word[1:]
                temp.append(capitalized_word)
    new_sentence = " "
    new_sentence = new_sentence.join(temp)
    return new_sentence

# o(n) slightly faster
def sentence_capitalization_second(sentence_string):
    result = sentence_string[0].upper()
    for i in range(1,len(sentence_string)):
        if sentence_string[i-1] == " ":
            result += sentence_string[i].upper()
        else: 
            result += sentence_string[i]
    return result

performance_tester([sentence_capitalization, sentence_capitalization_slice, sentence_capitalization_second], [
                   "I am a little tea pot", "and you can bet your box on a dollar", "the point cannot be explained in words reality is a concept here we are this is the express as you as you are we must go on"], n=500000, ylim=False)
