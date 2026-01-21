# создаём тестовую модель продукта 
import pytest 
from product.models import Product

@pytest.fixture 
def sample_product():
    return Product.objects.create(
        name = "Test Product",
        price = 100.00,
        in_stock = True
