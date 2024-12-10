import math 
import numpy as np

def custom_finite_diffrence_approach(f:callable,
                              x:float,
                              h:float,
                              points:list,
                              **kwargs):
    """
    Custom finite diffrence method for derivative approximation

    Args:
        f(function): Fuction of calculated to taking derivative
        x(float): Point of the calculated to taking derivative
        h:(float): Step size
        points(list): Position of the points eg.[0,1,2]
        **kwargs: Additional arguments(eg. precomputed coefficient with 'coeffs')
    Returns:
        float: Approximation of the derivative
    """
    coeffs = kwargs.get("coeffs")
    if coeffs is None:
        coeffs = calculate_custom_coefficients(points,h)
    
    if len(coeffs) != len(points):
        raise ValueError("Number of coefficients must be equal to the number of points")

    derivative = 0
    for point,coefficient in zip(points,coeffs):
        derivative += coefficient*f(x+point*h)
    
    return derivative/h

def taylor_coefficient_generator(h:float):
    """
    Calculate the taylor series coefficients

    Args:
        h(float): Step size
    Returns:
        list: Coefficients of the taylor series
    """
    i=0
    while True:
        yield h**i/math.factorial(i)
        i+=1

def calculate_custom_coefficients(points:list,h:float):
    pass 



if __name__=="__main__":
    f = lambda x: math.sin(x)
    x = math.pi
    h = 1.00e-6

    points_sets = [
        [0, 1, 2],  # 3-point forward 
        [-2, -1, 0, 1, 2],  # 5-point central
        [0, 1],  # 2-point forward  
        [0, 1, 2, 3],  # 4-point forward 
        [-1, 0, 1],  # 3-point central 
        [-2, -1, 0, 1],  # 4-point central 
        [-3, -2, -1, 0, 1]  # 5-point backward-central 
    ]

    for points in points_sets:
        result = custom_finite_diffrence_approach(f, x, h, points)
        print(f"Points {points}: {result}")
        print(f"Error: {abs(result - math.cos(x))}")

    print(f"\nTrue value: {math.cos(x)}")