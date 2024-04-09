import timeit

def profile_initial_test():
    """
    Tests the average execution time for test_initial_test function.

    Returns:
        float: Average execution time in seconds
    """

    SETUP = """from test import TestBindingEnergy"""
    TEST = """TestBindingEnergy.test_initial_test()"""

    number = 1000000
    total_execution_time = timeit.timeit(setup=SETUP, stmt=TEST, number=number)
    return total_execution_time/number

def profile_binding_energy():
    """
    Tests the average execution time for binding_energy function with the Cloud class.

    Returns:
        float: Average execution time in seconds
    """

    SETUP = """from binding_energy.cloud import Cloud"""
    TEST = """Cloud.binding_energy(6.82e-10)"""

    number = 1000000
    total_execution_time = timeit.timeit(setup=SETUP, stmt=TEST, number=number)
    return total_execution_time/number

def run_profiling():
    print("binding_energy execution time (s): " + str(profile_binding_energy()))
    print("initial_test execution time (s): " + str(profile_initial_test()))