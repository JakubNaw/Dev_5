import main as m
import pytest as pt
import math
import logging
import logging.handlers

def test_mul():
    a, b = 2, 2
    wynik = m.mul(a, b)
    assert math.isclose(a * b, wynik) == True

def test_mul_float():
    assert type(m.mul(2, 2)) == float

def test_div():
    a, b = 2, 2
    wynik = m.div(a, b)
    assert math.isclose(a / b, wynik) == True

def test_div_float():
    assert type(m.div(2, 2)) == float

def test_div_0():
    assert m.div(1, 0) is None

def test_sub():
    a, b = 2, 2
    wynik = m.sub(a, b)
    assert math.isclose(a - b, wynik)

def test_sub_float():
    assert type(m.sub(2, 2)) == float

def test_avg(caplog):
    m.avg()

    assert len(caplog.records) == 1
    assert caplog.records[0].message == 'warning'
