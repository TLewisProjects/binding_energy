import timeit

def profile_initial_test():
    """
    Tests the average execution time for initial_test function.

    Returns:
        float: Average execution time in seconds
    """

    SETUP = """from binding_energy.binding_energy import initial_test"""
    TEST = """initial_test()"""

    number = 1000000
    total_execution_time = timeit.timeit(setup=SETUP, stmt=TEST, number=number)
    return total_execution_time/number

def profile_binding_energy():
    """
    Tests the average execution time for binding_energy function.

    Returns:
        float: Average execution time in seconds
    """

    SETUP = """from binding_energy.binding_energy import binding_energy"""
    TEST = """binding_energy(6.82e-10)"""

    number = 1000000
    total_execution_time = timeit.timeit(setup=SETUP, stmt=TEST, number=number)
    return total_execution_time/number