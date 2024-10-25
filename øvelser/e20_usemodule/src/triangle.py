# Enter you module contents here

"""""
Module for right-angled triangle calculations.

This module contains functions to calculate the hypothenuse and the area
of a right-angled triangle.
"""
__version__ = '1.0'
__author__ = 'Darab'


import math

def hypothenuse(a, b):
    """
    Calculate the length of the hypothenuse of a right-angled triangle.
    
    Parameters:
    a (float): length of one side.
    b (float): length of the other side.
    
    Returns:
    float: length of the hypothenuse.
    """
    return math.sqrt(a**2 + b**2)

def area(a, b):
    """
    Calculate the area of a right-angled triangle.
    
    Parameters:
    a (float): length of one side.
    b (float): length of the other side.
    
    Returns:
    float: area of the triangle.
    """
    return 0.5 * a * b
