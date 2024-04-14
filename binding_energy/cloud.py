import math
import random

J_TO_EV = 6.24150907446076e+18

# Utility functions
def points_on_a_sphere(N, radius):
    """
    Generates a uniformly distributed set of points on the surface of a sphere.

        Args:
        N (int): The number of points to generate.
        radius (float): The radius of the sphere.

        Returns:
            list: A list of tuples containing the X, Y, and Z coordinates of each point.
    """
    points = []
    for i in range(N):
        z = random.uniform(-radius, radius)
        phi = random.uniform(0, 2*math.pi)

        x = math.sqrt((radius*radius)-(z*z))*math.cos(phi)
        y = math.sqrt((radius*radius)-(z*z))*math.sin(phi)

        points.append((x,y,z))

    return points

def write_sphere(file, N, radius):
    points = points_on_a_sphere(N, radius)
    with open(file, "w") as sphere_file:
        sphere_file.writelines([str(point[0])+","+str(point[1])+","+str(point[2])+"\n" for point in points])

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

    def total_binding_energy_brute(self, ev=False):
        """
        Calculates the total binding energy of a system of particles by direct summation.

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
        
    def total_binding_energy_cutoff(self, cutoff=None):
        """
        Calculates the total binding energy of a system of particles by direct summation
        with a hard cutoff in separation.

        Returns:
        float: The total binding energy of the particles.
        """
        # Set default cutoff if one is not provided.
        if(cutoff == None):
            cutoff = self.particle_size*10

        total_binding_energy = 0.0
        for index, particle in enumerate(self.system):
            # Slice to get all particles further along than the current one
            for other_particle in self.system[index+1:]:
                separation = particle.distance_to(other_particle)
                if(separation < cutoff):
                    total_binding_energy += self.binding_energy(separation, self.particle_size, self.dispersion_energy)
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