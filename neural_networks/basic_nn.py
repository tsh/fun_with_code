"""
Simple perception algorithm:
    1. For every input multiply that input by its weight
    2. Sum all of the weighted inputs
    3.  Compute the output of the perceptron based on that sum passed through an
        activation function.
"""
inputs = [12, 4]
weights = [0.5, -1]

sum_ = 0
for inp, weight in zip(inputs, weights):
    sum_ += inp * weight


def activate(sum_):
    return 1 if sum_ > 0 else -1

output = activate(sum_)