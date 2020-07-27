import string


def string_letter_count(s):
    character_list = list(string.ascii_lowercase)
    counter_list = [0] * 26
    s = s.lower()

    for character in s:
        for i, c in enumerate(character_list):
            if c == character:
                counter_list[i] += 1

    result = ""
    for counter, i in enumerate(counter_list):
        if i != 0:
            result += str(i)
            result += character_list[counter]
    return result


string_letter_count("aabz")
