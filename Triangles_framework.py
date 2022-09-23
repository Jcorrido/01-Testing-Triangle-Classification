# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):

    # for sorting the numbers from least to greatest
    numbers = [a,b,c]
    for n in numbers:
        if isinstance(n, int) != True:
            return "Not A Triangle"
    numbers.sort()

    # For setting up function for a^2 + b^2 = c^2
    d = numbers[0]**2 + numbers[1]**2
    e = numbers[2]**2

    # Note: This code is completely bogus but demonstrates a few features of python
    if numbers[0] + numbers[1] <= numbers[2]:
        return 'Not A Triangle'
    elif numbers[0] == numbers[1] and numbers[0] == numbers[2]:
        return 'Equilateral'
    elif numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[1] == numbers[2]:
        return 'Isoceles'
    elif d == e:
        return 'Right'
    else:
        return 'Scalene'



def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testMyTestSet2(self):
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(2,3,4),'Scalene')
        self.assertEqual(classifyTriangle(4,2,3), 'Scalene')
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles')
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isoceles')
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
        self.assertEqual(classifyTriangle(5, 4, 3), 'Right')
        self.assertEqual(classifyTriangle('a', 4, 3), 'Not A Triangle')


if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(2,3,4)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(2,2,3)
    runClassifyTriangle(3,4,5)

    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line




