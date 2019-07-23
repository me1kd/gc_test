# -*- coding: utf-8 -*-

import pytest
from gc_test.main import calculate

__author__ = "Kewei Duan"
__copyright__ = "Kewei Duan"
__license__ = "mit"


def test_calculate():
    assert calculate("A") == (50.0, [])
    assert calculate("AB") == (80.0, [])
    assert calculate("CDBA") == (115.0, [])
    assert calculate("AA") == (100.0, [])
    assert calculate("AAA") == (130.0, [])
    assert calculate("AAABB") == (175.0, [])
    with pytest.raises(AssertionError):
        calculate(None)
