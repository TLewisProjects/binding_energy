from math import sqrt as sqrt

class Particle():
    """
    Holds information on a single particle in a multi-particle system.
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other_particle):
        """
        Calculates the separation between two particle objects.

        Args:
        other_particle (Particle): Another object to calculate the distance to.

        Returns:
        float: The separation between this particle and other_particle.
        """
        x_separation = other_particle.x - self.x
        y_separation = other_particle.y - self.y
        z_separation = other_particle.z - self.z

        return sqrt((x_separation*x_separation) + 
                    (y_separation*y_separation) +
                    (z_separation*z_separation))