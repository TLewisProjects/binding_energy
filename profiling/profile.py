import timeit


def profile_initial_test():
    """
    Tests the average execution time for test_initial_test function.

    Returns:
        float: Average execution time in seconds.
    """

    SETUP = """from test.test_binding_energy import initial_test"""
    TEST = """initial_test()"""

    number = 1000000
    total_execution_time = timeit.timeit(setup=SETUP, stmt=TEST, number=number)
    return total_execution_time/number

def profile_binding_energy():
    """
    Tests the average execution time for binding_energy function with the Cloud class.

    Returns:
        float: Average execution time in seconds.
    """
    SETUP = """from binding_energy.cloud import Cloud"""
    TEST = """Cloud.binding_energy(6.82e-10, 3.41e-10, 1.65e-21)"""

    number = 1000000
    total_execution_time = timeit.timeit(setup=SETUP, stmt=TEST, number=number)
    return total_execution_time/number

def profile_sphere_test_brute():
    """
    Tests the average execution time for calculating the total binding energy 
    for a system of particles on the surface of a sphere.

    Returns:
        float: Average execution time in seconds.
    """
    SETUP = """from binding_energy.cloud import Cloud;import os"""
    TEST = """test_system = Cloud(os.path.join("test", "sphere_system.txt"));test_system.total_binding_energy_brute()"""
    
    number = 10
    total_execution_time = timeit.timeit(setup=SETUP, stmt=TEST, number=number)
    return total_execution_time/number

def profile_sphere_test_with_cutoff():
    """
    Tests the average execution time for calculating the total binding energy 
    for a system of particles on the surface of a sphere with a separation cutoff.

    Returns:
        float: Average execution time in seconds.
    """
    SETUP = """from binding_energy.cloud import Cloud;import os"""
    TEST = """test_system = Cloud(os.path.join("test", "sphere_system.txt"));test_system.total_binding_energy_cutoff()"""
    
    number = 10
    total_execution_time = timeit.timeit(setup=SETUP, stmt=TEST, number=number)
    return total_execution_time/number

def profile_sphere_test_hash():
    """
    Tests the average execution time for calculating the total binding energy 
    for a system of particles on the surface of a sphere with a separation cutoff
    and a hashtable.

    Returns:
        float: Average execution time in seconds.
    """
    SETUP = """from binding_energy.cloud import CloudHash;import os"""
    TEST = """test_system = CloudHash(os.path.join("test", "sphere_system.txt"));test_system.total_binding_energy()"""
    
    number = 10
    total_execution_time = timeit.timeit(setup=SETUP, stmt=TEST, number=number)
    return total_execution_time/number

def run_profiling():
    print("binding_energy execution time (s): " + str(profile_binding_energy()))
    print("initial_test execution time (s): " + str(profile_initial_test()))
    print("sphere_test brute execution time (s): " + str(profile_sphere_test_brute()))
    print("sphere_test cutoff execution time (s): " + str(profile_sphere_test_with_cutoff()))
    print("sphere_test hash execution time (s): " + str(profile_sphere_test_hash()))