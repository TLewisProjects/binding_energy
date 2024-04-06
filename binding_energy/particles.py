import math

from binding_energy import binding_energy

J_TO_EV = 6.24150907446076e+18

class Particles():

    def __init__(self, input_file):
        self.system = []
        with open(input_file) as input:
            for particle in input.readlines():
                x, y, z = particle.split(",")
                self.system.append(Particle(float(x),float(y),float(z)))

    def binding_energy(self, ev=False):
        """
        Calculates the total binding energy of a system of particles.

        Args:
        ev (Bool): If True, returns results in eV (electron-volts), else returns in J (joules)

        Returns:
        float: The total binding energy of the particles.
        """
        total_binding_energy = 0
        for index, particle in enumerate(self.system):
            # Slice to get all particles further along than the current one
            for other_particle in self.system[index+1:]:
                separation = particle.distance_to(other_particle)
                total_binding_energy += binding_energy.binding_energy(separation)

        if(ev):
            return total_binding_energy * J_TO_EV
        else:
            return total_binding_energy

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

        return math.sqrt((x_separation*x_separation) + 
                         (y_separation*y_separation) +
                         (z_separation*z_separation))

