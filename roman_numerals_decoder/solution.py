# https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python
def solution(roman):
    values = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}

    lwr = roman.lower()
    sum = 0
    lim = len(lwr) - 1
    handled = False
    for i, c in enumerate(lwr):
        if handled:
            handled = False
            continue
        if i == lim:
            sum += values[c]
            continue
        v = values[c]
        vn = values[lwr[i+1]]
        if v < vn:
            handled = True
            v = vn - v
        sum += v
    return sum
