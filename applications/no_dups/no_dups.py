def no_dups(s):
    # declare a dictionary
    dupless_dict = {}
    # split string on spaces to get array of words
    word_arr = s.split(" ")
    # loop over words arr
    for word in word_arr:
        # If the word doesn't exist in the dictionary, add it
        if dupless_dict.get(word) == None:
            dupless_dict[word] = 1
    # return the keys of the dictionary
    result = " ".join(list(dupless_dict.keys()))
    return result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))