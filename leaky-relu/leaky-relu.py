import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here

    arr = np.array(x)

    result = np.where(arr <= 0, arr*alpha, arr)

    return result
    pass