import random

class Perceptron(object):
    def __init__(self, weights_length):
        self.weights = [random.uniform(-1, 1) for _ in range(weights_length)]

    def feedforward(self, inputs):
        """
        Perception function which takes input and generates output of the Perceptron
        """
        sum_ = 0
        for inp, weight in zip(inputs, self.weights):
            sum_ += inp * weight
        return self.activate(sum_)

    def activate(self, sum_):
        return 1 if sum_ > 0 else 0


def train_network():
    """
    Trains the nn to obtain correct result. The process is as follows:
        1. Provide the perceptron with inputs for which there is a known answer.
        2. Ask the perceptron to guess an answer.
        3. Compute the error. (Did it get the answer right or wrong?)
        4. Adjust all the weights according to the error.
        5. Return to Step 1 and repeat!
    """


if __name__ == '__main__':
    perceptron = Perceptron(3)
    inputs = [50, -12, 1]
    result = perceptron.feedforward(inputs)