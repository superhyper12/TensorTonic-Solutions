import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """


    arr = np.array(x)
    result = np.where(arr <= 0, 0, arr)

    return result
    
    pass