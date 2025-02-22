# Файл для хранения фикстур
import pytest

from src.taxes import calculate_taxes


@pytest.fixture
def fixt_1():
    return [110.0, 220.0, 330.0, 440.0]



