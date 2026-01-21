from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100) # поле с ограничением по символам
    price = models.DecimalField(max_digits=10,decimal_places=2) # спец поле для денег digits и decimial обязательные поля для преедачи 
    in_stock = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # создаём простой метод
    def apply_discount(self,percent):
        #прининяем скидку к товару
        self.price = self.price*(100-percent)/100
        self.save()
