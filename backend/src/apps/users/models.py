from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Кастомная модель пользователя
    # username - уже создано в Абстрактном пользователе
    # passsword - уже создано в Абстрактном пользователе
    # Добавим опциональные поля:
    email = models.EmailField(unique=True,null=False)
    # Поле для большого количества текста(str)
    description = models.TextField()
    # Поле для символов определенного количества с ограничение - максимум 255
    phone = models.CharField(max_length = 11, unique=True,blank=True,null=True)
    # Два вида поля для картинок
    avatar = models.ImageField(upload_to='avatars/')
    # Если вы храните не у себя в сервере картинки, храните их на удалёнке или даёте загрузить аватар по ссылке
    image = models.URLField()
    
    # Добавляем флажок аутенцикафии группы людей и также задаём related_name для избежания конфликтов
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user',
        blank=True
    )
    
    def __str__(self):
        return self.username
    
    