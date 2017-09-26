# Convert a tuple to String
def tupletostr(tarTuple):
    res = ''
    for a in tarTuple:
        if type(a) is type(tarTuple):
            res += tupletostr(a)
        else:
            res += str(a)
    return res