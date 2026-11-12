from django.db import models
class Product(models.Model):
    name = models.CharField('Название', max_length=200)
    cost = models.CharField('Цена', max_length=50)
    photo_url = models.URLField("Ссылка на фото", max_length= 500, blank=True, null= True, help_text="Вставьте ссылку (https://)")
    description = models.TextField('Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    bought = models.BooleanField('Куплено', default=False)
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name

class Order(models.Model):
    title = models.CharField('Продавец', max_length=200)
    description = models.TextField('Описание')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    