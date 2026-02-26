import numpy as np

def FizzBuzz(first, last):
    nums = np.arange(first, last + 1)
    out = np.array(nums, dtype=object)

    fizz = nums % 3 == 0
    buzz = nums % 5 == 0

    out[fizz] = "fizz"
    out[buzz] = "buzz"
    out[fizz & buzz] = "fizzbuzz"

    return out