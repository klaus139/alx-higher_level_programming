#!/usr/bin/python3
def multipe_returnss(sentence):
    "return a tuple with the lenght of a string and its first character"

    "if the sentence is empty, the first character should be equal to None"
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
