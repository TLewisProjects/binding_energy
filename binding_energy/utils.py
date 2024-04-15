from random import random_uniform
from math import pi as PI
from math import cos
from math import sin
from math import sqrt

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
        z = random_uniform(-radius, radius)
        phi = random_uniform(0, 2*PI)

        x = sqrt((radius*radius)-(z*z))*cos(phi)
        y = sqrt((radius*radius)-(z*z))*sin(phi)

        points.append((x,y,z))

    return points

def write_sphere(file, N, radius):
    points = points_on_a_sphere(N, radius)
    with open(file, "w") as sphere_file:
        sphere_file.writelines([str(point[0])+","+str(point[1])+","+str(point[2])+"\n" for point in points])
