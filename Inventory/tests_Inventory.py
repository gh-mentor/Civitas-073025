from Inventory.models import Product
import pytest
from datetime import datetime, timedelta
import time

# Python

def test_update_quantity_increases():
    product = Product(quantity=10)
    before_update = product.updated_at
    time.sleep(0.01)  # Ensure updated_at will be different
    product.update_quantity(5)
    assert product.quantity == 15
    assert product.updated_at > before_update

def test_update_quantity_decreases():
    product = Product(quantity=10)
    before_update = product.updated_at
    time.sleep(0.01)
    product.update_quantity(-3)
    assert product.quantity == 7
    assert product.updated_at > before_update

def test_update_quantity_zero():
    product = Product(quantity=10)
    before_update = product.updated_at
    time.sleep(0.01)
    product.update_quantity(0)
    assert product.quantity == 10
    assert product.updated_at > before_update