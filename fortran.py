# fortran specific functions


def SIGN(A, B):
    # returns the value of A with the fortran.sign of B
    if B < 0:
        return -A
    return A
    # TODO: или всё-таки так?
    #     return -abs(A)
    # return abs(A)


def DO(A, B, STEP=1):
    # returns iterable like python range
    return range(A, B+1, STEP)
