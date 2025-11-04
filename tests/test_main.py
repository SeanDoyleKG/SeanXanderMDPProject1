import pytest
from src.main import makelist

def test_basic():
    assert 1 == 1

def test_makelist():
    lst = []
    assert makelist(lst) == 1