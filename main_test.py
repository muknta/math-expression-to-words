import pytest
from main import math_to_str as mts


def test_answer():
    assert mts('1 + 3 = 4') == 'one plus three equals four'
    assert mts('1+ 3 = 4') == 'invalid input'
    assert mts('') == ''
    assert mts('ir232 =') == 'invalid input'
    assert mts('11 + 3 = 4') == 'eleven plus three equals four'
    assert mts('= ( ) + - 312 4 1 * ^ / 0') == 'equals left bracket right bracket plus minus three hundred and twelve four one multiplicate raise to the power of divide zero'
    assert mts('   +   ') == 'plus'
    assert mts('8   10   ') == 'eight ten'
    assert mts('724209') == 'seven hundred and twenty-four thousand, two hundred and nine'

