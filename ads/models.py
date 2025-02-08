from django.db import models
from django.conf import settings
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name

class Ad(models.Model):
    STATUS_CHOICES = [
        ("moderation", "На модерации"),
        ("published", "Опубликовано"),
        ("rejected", "Отклонено"),
        ("deleted", "На удаление"),
    ]

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="moderation", verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    published_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    def save(self, *args, **kwargs):
        if self.pk and self.status == "published" and not kwargs.get("force_update", False):
            self.status = "moderation"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

def get_absolute_url(self):
    return reverse("ad-detail", kwargs={"pk": self.pk})
