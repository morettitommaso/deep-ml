def activation(x):
    '''
    Apply an activation function element-wise.
    
    Args:
        x: numpy array of any shape (raw neuron outputs)
    
    Returns:
        numpy array of same shape (activated outputs)
    
    Requirements:
        - Must be non-linear (not just returning x)
        - Must work on arrays of any shape
        - Must be deterministic
    '''
    # TODO: Implement your activation function
    import numpy as np
    list_out = []

    def ReLU(x):
        return x * (x > 0)

    def relu_max(x):
        out = np.maximum(x, 0)
        return out

    for i in x:
        list_out.append(relu_max(i))

    return np.array(list_out)
