import pytest

from src.taxes import calculate_taxes


def test_calculate_taxes():
    assert (calculate_taxes([100.0, 200.0, 300.0, 400.0], 10) ==
            [110.0, 220.0, 330.0, 440.0])

def test_calc_tax_fixt_1(fixt_1):
    assert calculate_taxes([100.0, 200.0, 300.0, 400.0], 10) == fixt_1

def test_calc_tax_zero():
    with pytest.raises(ValueError) as exec_info:
        calculate_taxes([0.0], 10.0)
    assert str(exec_info.value) == "Неверная цена"

def test_calc_tax_negative():
    with pytest.raises(ValueError) as exec_info:
        calculate_taxes([10, 20], -10)
    assert str(exec_info.value) == "Неверный налоговый процент"




