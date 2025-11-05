import pytest

#function to test sqaure
def square(n):
    return n ** 2

#function to test cube

def cube(n):
    return n ** 3

def fifth(n):
    return n ** 5


#testing the square function
def test_sqaure():
    assert square(2) == 4, "Test Failed : Sqaure of 2 should be 4"
    assert square(3) == 9, "Test Failed : Sqaure of 2 should be 4"

#testing the cube function
def test_cube():
    assert cube(2) == 8, "Test Failed : Sqaure of 2 should be 8"
    assert cube(3) == 27, "Test Failed : Sqaure of 2 should be 27"


def test_fifth():
    assert fifth(2) == 32, "Test Failed : Sqaure of 2 should be 32"
    assert fifth(3) == 243, "Test Failed : Sqaure of 2 should be 243"
    
    
#test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
        
    