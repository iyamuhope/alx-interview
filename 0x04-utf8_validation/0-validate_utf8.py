#!/usr/bin/python3
""" Validate UTF-8 """


def validUTF8(data):
    """ Determines if a given data set represents valid UTF-b Encoding """
    count = 0

    for x in data:
        if 191 >= x >= 128:
            if not count:
                return False
        else:
            if count:
                return False
            if x < 128:
                continue
            elif x < 224:
                count = 1
            elif x < 240:
                count = 2
            elif x < 248:
                count = 3
            else:
                return False

    return count == 0
