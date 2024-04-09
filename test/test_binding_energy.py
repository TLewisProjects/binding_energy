import unittest
import os

from numpy.testing import assert_allclose
from binding_energy import binding_energy

from binding_energy.particles import Particles

script_dir = os.path.dirname(__file__)

class TestBindingEnergy(unittest.TestCase):
    def test_binding_energy(self):
        """
        Test single binding energy calculation
        """
        assert_allclose(binding_energy.binding_energy(6.82e-10), -1.0e-22, rtol=1e-1)

    def test_initial_test(self):
        """
        Test initial case from technical exercise
        """
        assert_allclose(binding_energy.initial_test(), 3.819639045e-18)

    def test_zero_system_2(self):
        """
        Test a system of two particles equidistant by particle size.
        """
        test_system = Particles(os.path.join(script_dir, "zero_system_2.txt"))
        assert_allclose(test_system.binding_energy(ev=True), 0.0)

    def test_zero_system_3(self):
        """
        Test a system of three particles equidistant by particle size.
        """
        test_system = Particles(os.path.join(script_dir, "zero_system_3.txt"))
        assert_allclose(test_system.binding_energy(ev=True), 0.0, atol=1e-16)


if __name__ == "__main__":
    unittest.main()