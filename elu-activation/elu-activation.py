import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    result = []

    for i in range(len(x)):
        if x[i] <= 0:
            val =  alpha * (math.exp(x[i]) - 1)
            result.append(val)
        else:
            result.append(x[i])
            
    
    return result
    
    pass