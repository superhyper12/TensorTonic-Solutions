import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    arr = np.array(x)
    
    result = 1 / (1+ np.exp(-arr))

    return result
    pass