#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""
import math

def hypotenuse(x,y):
    return math.pow((math.pow(x,2) + math.pow(y,2)),1/2)

assert hypotenuse(6,8) == 10