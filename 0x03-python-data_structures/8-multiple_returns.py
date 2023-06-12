#!/usr/bin/python3
def multiple_returns(sentence):
  """Return length of string and the first character."""
    len_sen = len(sentence)

    if (len_sen == 0):
        new_tuple = (len_sen, None)
    else:
        new_tuple = (len_sen, sentence[0])

    return (new_tuple)
