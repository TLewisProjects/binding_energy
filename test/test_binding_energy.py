import unittest
import os

from numpy.testing import assert_allclose

from binding_energy.cloud import Cloud, CloudHash

script_dir = os.path.dirname(__file__)

# Define model parameters
PARTICLE_SIZE = 3.41e-10
DISPERSION_ENERGY = 1.65e-21

def initial_test():
    """
    The initial test case from the technical exercise.
    """
    object_separations = [4.1e-10, 2e-10, 3.41e-10]

    total_binding_energy = 0
    for r in object_separations:
        total_binding_energy += Cloud.binding_energy(r, PARTICLE_SIZE, DISPERSION_ENERGY)
    return total_binding_energy

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
        assert_allclose(initial_test(), 3.819639045e-18)

    def test_zero_system_2(self):
        """
        Test a system of two particles equidistant by particle size.
        """
        test_system = Cloud(os.path.join(script_dir, "zero_system_2.txt"))
        assert_allclose(test_system.total_binding_energy_brute(ev=True), 0.0)

    def test_zero_system_3(self):
        """
        Test a system of three particles equidistant by particle size.
        """
        test_system = Cloud(os.path.join(script_dir, "zero_system_3.txt"))
        assert_allclose(test_system.total_binding_energy_brute(ev=True), 0.0, atol=1e-16)

    def test_sphere_system_brute(self):
        """
        Test a system of particles on the surface of a sphere with direct summation.
        """
        test_system = Cloud(os.path.join(script_dir, "sphere_system.txt"))
        assert_allclose(test_system.total_binding_energy_brute(), 348695.0999843)

    def test_sphere_system_cutoff(self):
        """
        Test a system of particles on the surface of a sphere with a cutoff.
        """
        test_system = Cloud(os.path.join(script_dir, "sphere_system.txt"))
        assert_allclose(test_system.total_binding_energy_cutoff(), test_system.total_binding_energy_brute())

    def test_sphere_system_with_hash(self):
        test_system_hash = CloudHash(os.path.join(script_dir, "sphere_system.txt"))
        test_system_brute = Cloud(os.path.join(script_dir, "sphere_system.txt"))
        assert_allclose(test_system_hash.total_binding_energy(), test_system_brute.total_binding_energy_brute())

if __name__ == "__main__":
    unittest.main()