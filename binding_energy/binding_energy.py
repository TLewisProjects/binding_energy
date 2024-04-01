from typing import Type

SCALE_FACTOR = 3.41e-10
EPSILON = 1.65e-21

def binding_energy(r):
    """
    Calcuate the binding energy for two objects with separation, r.

    Args:
        r (float): The separation of two objects

    Returns:
        float: The binding energy
    """
    scaled_r = SCALE_FACTOR / r # pre-calculate scale
    return 4*EPSILON*(pow(scaled_r, 12) - pow(scaled_r, 6))

def initial_test():
    object_separations = [4.1e-10, 2e-10, 3.41e-10]

    total_binding_energy = 0
    for r in object_separations:
        total_binding_energy += binding_energy(r)
    
    return total_binding_energy
