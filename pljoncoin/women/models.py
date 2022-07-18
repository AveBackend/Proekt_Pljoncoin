from django.db import models
class Women(models.Model):
    nickname = models.CharField(max_length=16, verbose_name = 'Имя пользователя')
    mail = models.CharField(max_length=22, verbose_name = 'Почта пользователя')
    password = models.CharField(max_length=32, verbose_name ='Пароль пользователя')
    password_remain = models.CharField(max_length=32,)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время регистрации')
    time_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Зарегистрированные пользователи'
        verbose_name_plural = 'Зарегистрированные пользователи'
        ordering = ['time_create', 'nickname']

    class Category(models.Model):
        name = models.CharField(max_length=100, db_index = True)

        def __str__(self):
            return self.name
