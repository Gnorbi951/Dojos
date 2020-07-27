def solution(string, ending):
    if len(ending) == 0:
        return True

    if string[(-1*len(ending))::] == ending:
        return True
    else:
        return False


solution("abcde", "cde")
