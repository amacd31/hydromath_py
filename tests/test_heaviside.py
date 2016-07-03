import unittest

import numpy as np

from hydromath import heaviside

class HeavisideTestCase(unittest.TestCase):

    def setUp(self):
        self.test_input = np.array([1,2,3,4,5,6,7,6,5,4,3,2,1], dtype=np.float)

    def tearDown(self):
        pass

    def test_heaviside(self):
        result = heaviside(self.test_input, 5)

        self.assertEqual(sum(result), 5)
        self.assertEqual(len(result), 13)


if __name__ == '__main__':
    unittest.main()
