from typing import Type

PARTICLE_SIZE = 3.41e-10
DISPERSION_ENERGY = 1.65e-21

def binding_energy(r):
    """
    Calcuate the binding energy for two objects with separation, r.

    Args:
        r (float): The separation of two objects

    Returns:
        float: The binding energy
    """
    scaled_r = pow(PARTICLE_SIZE / r,6)
    return 4*DISPERSION_ENERGY*(scaled_r)*(scaled_r-1)

def initial_test():
    """
    Calcuate the total binding energy for a set of three objects at fixed separations.

    Returns:
        float: The total binding energy
    """
    object_separations = [4.1e-10, 2e-10, 3.41e-10]

    total_binding_energy = 0
    for r in object_separations:
        total_binding_energy += binding_energy(r)
    
    return total_binding_energy
