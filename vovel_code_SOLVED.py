# Clever solution
# tbl1 = str.maketrans("aeiou", "12345")
# tbl2 = str.maketrans("12345", "aeiou")
# return st.translate(tbl1)


def encode(st):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    output = ""
    for char in st:
        if char in vowels:
            if char == "a":
                output += "1"
            if char == "e":
                output += "2"
            if char == "i":
                output += "3"
            if char == "o":
                output += "4"
            if char == "u":
                output += "5"

        else:
            output += char
    return output


def decode(st):

    output = ""
    for char in st:
        if char == "1":
            output += "a"
        if char == "2":
            output += "e"
        if char == "3":
            output += "i"
        if char == "4":
            output += "o"
        if char == "5":
            output += "u"

        elif char.isalpha():
            output += char
    return output


print(encode("hello there"))
print(decode("h2ll4 th2r2"))
