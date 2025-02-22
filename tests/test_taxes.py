import pytest

from src.taxes import calculate_taxes, calculate_tax


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


@pytest.mark.parametrize("prices, tax, result", [
    ([10, 20, 30], 10, [11, 22, 33]),
    ([10, 20, 30], 100, [20, 40, 60]),
    ([10, 20, 30], 50, [15, 30, 45])
])
def test_calc_tax_param(prices, tax, result):
    assert calculate_taxes(prices, tax) == result

@pytest.mark.parametrize("price, tax, result", [(100, 10, 110), (50, 5, 52.5)])
def test_calculate_tax_normal(price, tax, result):
    assert calculate_tax(price, tax) == result

def test_calculate_tax_negative_price():
    with pytest.raises(ValueError):
        calculate_tax(-10, 10)

def test_calculate_tax_negative():
    with pytest.raises(ValueError):
        calculate_tax(10, -10)

def test_calculate_tax_more_than_100():
    with pytest.raises(ValueError):
        calculate_tax(10, 110)

def test_calculate_tax_100():
    with pytest.raises(ValueError):
        calculate_tax(10, 100)

def test_calculate_tax_discount():
    assert calculate_tax(100, 10, discount=5) == 104.5

def test_calculate_tax_discount_zero():
    assert calculate_tax(100, 10) == 110

def test_calculate_tax_discount_round():
    assert calculate_tax(95, 11, discount=5, round_dig=3) == 100.177

def test_calculate_tax_discount_round_default():
    assert calculate_tax(95, 11, discount=5) == 100.18

@pytest.mark.parametrize("round_dig, expected", [(0, 99),
                                                 (1, 99.4),
                                                 (2, 99.42),
                                                 (3, 99.425)])
def test_calculate_tax_discount_round_new(round_dig, expected):
    assert calculate_tax(100, 2.5, discount=3, round_dig=round_dig) == expected


def test_calculate_tax_discount_round_with_type():
    with pytest.raises(TypeError):
        calculate_tax("2", "11", discount="5")
