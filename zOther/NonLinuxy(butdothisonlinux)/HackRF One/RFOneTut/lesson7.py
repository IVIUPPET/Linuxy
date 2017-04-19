import cmath
tau = 2 * pi
def average(readings):
    base = e ** (1j * tau / 360) //comment
    total = 0
    for r in readings:
        total += base ** r //vec addition
    result = total / len(readings) //avg vectors
    return cmath.log(result, base).real // use log to conv back from cplex plane to deg

