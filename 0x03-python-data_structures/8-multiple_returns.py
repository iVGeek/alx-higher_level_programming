#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        len_s = len(sentence)
        return((len_s, sentence[0]) if len_s != 0 else (None, sentence[0]))
