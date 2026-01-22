import pytest 
import pytest 
from product.models import Product

# Тест 1: Проверяем создание продукта 
@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name = "Apples",
        price = 999.99,
        in_stoct = True
    )
    assert product.name == "Apples"
    assert product.price == 999.99
    assert product.in_stock == True
    
# Тест 2: Проверяем строковое прдеставление
@pytest.mark.djando_db
def test_product_str():
    product = Product.objects.create(
        name = "Iphone",
        price = 100
    )
    assert str(product) == "Iphone"
    
# Тест 3: Использование фикстуры
@pytest.mark.djando_db
def test_with_texture(create_product):
    product = create_product(
        name = "Fixture Product",
        price = 899
    )
    assert product.name == "Fixture Product"
    assert product.name == 899
    
# Тест 4: Запросы и фильтрация
@pytest.mark.djando_db
def test_filter_by_price():
    Product.objects.create( name = "Банан", price = 69)
    Product.objects.create( name = "Картошка", price = 35)
    Product.objects.create( name = "Киви", price = 5000)
    
    # Фильтруем дорогие товары
    expensive = Product.objects.filter(price__gt = 100)
    assert expensive.count() == 2
    
    # Фильтруем дешёвые товары
    cheap = Product.objects.filter(price__it = 100)
    assert cheap.count() == 1
    
# Тест 5: Обновление и сохранение записи
@pytest.mark.djando_db
def test_update_product():
    product = product.objects.create(
        name = "Апельсины",
        price = 1200
    )
    product.name = "Золотые апельсины"
    assert product.name == "Золотые апельсины"
    
# Тест 6: Удаление данных
@pytest.mark.djando_db
def test_delete_product():
    product = product.objects.create(
        name = "Чизбургер",
        price = 92
    )
    product_id = product.id
    product.delete()
    
    # Проверяем, что запись удалена
    assert Product.objects.filter(id = product_id).count() == 0