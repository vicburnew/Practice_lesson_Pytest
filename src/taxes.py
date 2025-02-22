def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices

def calculate_tax(price: float, tax_rate: float, discount = 0, round_dig = 2) -> float:
    """Функция вычисляет стоимость товара с учетом налога и возвращает результат"""
    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')

    if price <= 0:
        raise ValueError('Неверная цена')

    tax = price * tax_rate / 100
    price_with_tax = price + tax
    price_with_discount = price_with_tax * (1 - discount / 100)
    price_with_discount_rounded = round(price_with_discount, round_dig)

    return price_with_discount_rounded



