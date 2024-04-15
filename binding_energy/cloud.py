import math
import random
import pdb

from argparse import ArgumentParser
from itertools import product as itertools_product

from binding_energy.hashtable import HashTable

from binding_energy.particle import Particle

J_TO_EV = 6.24150907446076e+18

class CloudBrute():
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

        Args:
        cutoff (float): The maximum separation at which the binding energy is no longer evaluated.

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
    

class Cloud():
    def __init__(self, input_file, particle_size=3.41e-10, dispersion_energy=1.65e-21, cutoff=10, hashtable_bin_size=5):
        """
        Initialises the system.

        Args:
        input_file (str): A filepath to a text file containing the 3D positions of the particles in the system.
        particle_size (float): Size of the particles in the system in metres (sigma).
        dispersion_energy (float): Depth of the potential well in joules (epsilon).
        cutoff (float): Maximum separation between two particles for which the binding energy is calculated.
        hashtable_bin_size (float): The size of the bins in the HashTable as a proportion particle_size.
        """
        self.hash_system = HashTable(particle_size*hashtable_bin_size)

        with open(input_file) as input:
            for particle in input.readlines():
                x, y, z = particle.split(",")
                self.hash_system.insert(Particle(float(x), float(y), float(z)))

        self.particle_size = particle_size
        self.dispersion_energy = dispersion_energy
        self.cutoff = particle_size*cutoff

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
    
    def total_binding_energy(self):
        """
        Calculates the total binding energy of a system of particles
        with a hard cutoff in separation.

        Returns:
        float: The total binding energy of the particles.
        """
        total_binding_energy = 0.0
        cutoff_in_cells = math.ceil(self.cutoff/self.hash_system.gridcell_size)

        for key, value in self.hash_system.table.items():
            X, Y, Z = key
            max_X = X + cutoff_in_cells
            min_X = X - cutoff_in_cells
            max_Y = Y + cutoff_in_cells
            min_Y = Y - cutoff_in_cells
            max_Z = Z + cutoff_in_cells
            min_Z = Z - cutoff_in_cells

            # Create list of all neighbours within cutoff
            neighbour_cells = list(itertools_product([x for x in range(min_X,max_X+1)],
                                                 [y for y in range(min_Y,max_Y+1)],
                                                 [z for z in range(min_Z,max_Z+1)]))
            
            # Iterate through positions in cell list
            for particle in value:
                # Iterate over neighbouring cells within cutoff
                for neighbour_cell in neighbour_cells:
                    neighbours = self.hash_system.retrieve_by_hash(neighbour_cell)
                    for neighbour in neighbours:
                        if(neighbour != particle):
                            # Add binding energy to total
                            total_binding_energy += self.binding_energy(particle.distance_to(neighbour), 
                                                                    self.particle_size, 
                                                                    self.dispersion_energy)
        # Account for double-counting
        return 0.5*total_binding_energy

if __name__ == "__main__":
    # Handle user input from the command line
    parser = ArgumentParser(prog="Cloud simulator", 
                            description="""Calculate state quantities of a multi-particle system - 
                            currently only total binding energy""")
    
    parser.add_argument("filepath", help="""The file location of a text file containing the initial 3D
                        spatial positions of a set of particles. Each particle position should be on a separate line
                        and the X, Y, and Z positions should be separated by commas.""")
    parser.add_argument("-p", "--particle_size", default=3.41e-10, help="The sigma value for the Lennard-Jones potential.")
    parser.add_argument("-d", "--dispersion_energy", default=1.65e-21, help="The epsilon value for the Lennard-Jones potential.")

    args = parser.parse_args()
    filepath = args.filepath
    particle_size = args.particle_size
    dispersion_energy = args.dispersion_energy

    system = Cloud(filepath, particle_size=particle_size, dispersion_energy=dispersion_energy)

    total_binding_energy = system.total_binding_energy_cutoff()
    print("Total binding energy of your system: "+str(total_binding_energy)+" J")