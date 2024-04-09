import unittest
import os

from numpy.testing import assert_allclose
from binding_energy import binding_energy

from binding_energy.cloud import Cloud

script_dir = os.path.dirname(__file__)

# Define model parameters
PARTICLE_SIZE = 3.41e-10
DISPERSION_ENERGY = 1.65e-21

class TestBindingEnergy(unittest.TestCase):
    def test_binding_energy(self):
        """
        Test single binding energy calculation.
        """
        assert_allclose(Cloud.binding_energy(6.82e-10, PARTICLE_SIZE, DISPERSION_ENERGY), -1.0e-22, rtol=1e-1)

    def test_initial_test(self):
        """
        Test initial case from technical exercise.
        """
        object_separations = [4.1e-10, 2e-10, 3.41e-10]

        total_binding_energy = 0
        for r in object_separations:
            total_binding_energy += Cloud.binding_energy(r, PARTICLE_SIZE, DISPERSION_ENERGY)
        assert_allclose(total_binding_energy, 3.819639045e-18)

    def test_zero_system_2(self):
        """
        Test a system of two particles equidistant by particle size.
        """
        test_system = Cloud(os.path.join(script_dir, "zero_system_2.txt"))
        assert_allclose(test_system.binding_energy(ev=True), 0.0)

    def test_zero_system_3(self):
        """
        Test a system of three particles equidistant by particle size.
        """
        test_system = Cloud(os.path.join(script_dir, "zero_system_3.txt"))
        assert_allclose(test_system.binding_energy(ev=True), 0.0, atol=1e-16)


if __name__ == "__main__":
    unittest.main()