def ftoi(f: float) -> int:
    return int(f + 0.5)
    
def frange(start, end, step: float):
    val = start
    ret = [val]

    while val < (end - step):
        val += step
        ret.append(val)

    return ret
    