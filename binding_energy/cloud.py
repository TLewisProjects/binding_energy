import math

J_TO_EV = 6.24150907446076e+18

class Cloud():
    """
    Holds information on a multi-particle system in 3D space.
    """
    
    def __init__(self, input_file, particle_size=3.41e-10, dispersion_energy=1.65e-21):
        """
        Initialises the system.

        Args:
        input_file (str): A filepath to a text file containing the 3D positions of the particles in the system.
        particle_size (float): Size of the particles in the system in metres (sigma).
        dispersion_energy (float): Depth of the potential well in joules (epsilon).
        """
        self.system = []
        with open(input_file) as input:
            for particle in input.readlines():
                x, y, z = particle.split(",")
                self.system.append(Particle(float(x),float(y),float(z)))

        self.particle_size = particle_size
        self.dispersion_energy = dispersion_energy

    @staticmethod
    def binding_energy(r, particle_size, dispersion_energy):
        """
        Calcuate the binding energy for two objects with separation, r.

        Args:
            r (float): Separation of two objects.
            particle_size (float): Size of the particles involved in metres.
            dispersion_energy (float): Depth of the potential well in joules

        Returns:
            float: The binding energy
        """
        scaled_r = pow(particle_size / r,6)
        return 4*dispersion_energy*(scaled_r)*(scaled_r-1)

    def total_binding_energy(self, ev=False):
        """
        Calculates the total binding energy of a system of particles.

        Args:
        ev (Bool): If True, returns result in eV (electron-volts), else returns in J (joules)

        Returns:
        float: The total binding energy of the particles.
        """
        total_binding_energy = 0.0
        for index, particle in enumerate(self.system):
            # Slice to get all particles further along than the current one
            for other_particle in self.system[index+1:]:
                separation = particle.distance_to(other_particle)
                total_binding_energy += self.binding_energy(separation, self.particle_size, self.dispersion_energy)

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