import numpy as np

def prod_signs(arr):
    if not arr:
        return None
    sign_product = np.prod(np.sign(arr))
    magnitude_sum = sum(abs(x) for x in arr)
    return magnitude_sum * sign_product
