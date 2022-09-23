from django.db import models

class BD(models.Model):
    login = models.CharField("Логин:", max_length=30)
    password = models.CharField("Пароль:", max_length=30)


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
# Create your models here.
