import unittest
from neural_network import Neuron, Connection, NeuralNetwork, Innovations

class Test_test_1(unittest.TestCase):
    def test_network_size(self):
        self.global_innovations = Innovations(0, {}) # initialize global innovations object
        self.nn = NeuralNetwork(5, 0, 5, [], [], self.global_innovations)

        self.assertTrue(self.nn.network_size() == 10)

    def test_weight_mutation(self):
        self.n_in = Neuron(1.0, [], [], 1, 1)
        self.n_out = Neuron(0, [], [], 3, 2)

        self.test_conn = Connection(self.n_in, self.n_out, 0, 1)

        self.assertTrue(-1.0 <= self.test_conn.weight <= 1.0)
        self.test_conn.mutate_weight()
        self.assertTrue(-1.0 <= self.test_conn.weight <= 1.0)


if __name__ == '__main__':
    unittest.main()
