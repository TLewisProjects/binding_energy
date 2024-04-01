import unittest
import math

from numpy.testing import assert_allclose
from binding_energy import binding_energy

class TestBindingEnergy(unittest.TestCase):
    def test_binding_energy(self):
        assert_allclose(binding_energy.binding_energy(6.82e-10), -1.0e-22, rtol=1e-1)

if __name__ == "__main__":
    unittest.main()