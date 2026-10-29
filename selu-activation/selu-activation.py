import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    l = 1.0507
    a = 1.67326
    
    result = []
    for i in range(len(x)):
        if x[i] <= 0:
            val = l * a * (math.exp(x[i]) - 1)
            result.append(val)
        else:
            val2 = l * x[i]
            result.append(val2)

    return result
    
    pass