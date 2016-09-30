import numpy as np
from pytest import raises
from binsearch import binary_search

def test_doc():
    input=list(range(10))
    assert binary_search(input,5) == 5
    assert binary_search(input, 4.5)==-1
#    assert binary_search(input, 10) == -1
# We have treated this case as an needle too large error
    assert binary_search([5], 5) == 0
    assert binary_search([1,2,np.inf], np.inf)==2
    assert binary_search(input, 5, 1,3)==-1
    assert binary_search(input, 2, 1,3)==2
    assert binary_search(input, 2, 3, 1)==-1
    assert binary_search(input, 2, 2, 2)==2
    assert binary_search(input, 5, 2, 2)==-1




def test_notlist():
    with raises(TypeError):
        binary_search(5,2)

def test_zerolist():
    with raises(ValueError):
        binary_search([],2)       
        
def test_char():
    with raises(TypeError):
        binary_search(['a',3],1)
        
def test_largerneedle():
    with raises(ValueError):
        binary_search([1,4,5,7],10)

def test_smallerneedle():
    with raises(ValueError):
        binary_search([1,4,5,7],0)
def test_misselement():
    with raises(TypeError):
        binary_search([1,np.nan,5,6],5)