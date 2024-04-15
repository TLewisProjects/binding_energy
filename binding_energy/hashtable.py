from binding_energy.particle import Particle

class HashTable():
    """
    Basic hashtable implementation using dictionaries.
    """

    def __init__(self, gridcell_size):
        """
        Initialises the hashtable.

        Args:
        gridcell_size (float): Size of hashtable cells in all three dimensions.

        """
        self.table = {}
        self.gridcell_size = gridcell_size

    def hash(self, position):
        """
        Hashes a 3D position.

        Args:
        position (list or tuple): A 3D position.

        Returns:
        tuple: Hashed version of position.
        """
        return (int(position[0]/self.gridcell_size), int(position[1]/self.gridcell_size), int(position[2]/self.gridcell_size))
    
    def insert(self, particle):
        """
        Inserts a Particle object into the appropriate cell in the hashtable.

        Args:
        particle (Particle): A Particle object that is going to be inserted into the hashtable.

        """
        hash = self.hash((particle.x, particle.y, particle.z))
        if(hash in self.table):
            self.table.get(hash).append(particle)
        else:
            self.table[hash] = [particle]
    
    def retrieve_by_hash(self, hash):
        """
        Access cell contents by hash value.

        Args:
        hash (tuple): A tuple representing a 3D position.

        Returns:
        The contents of the hashtable cell if occupied [] otherwise.

        """
        if(hash in self.table):
            return self.table.get(hash)
        else:
            return []
