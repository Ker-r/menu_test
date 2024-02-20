from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    title = models.CharField(
        'Название пункта меню',
        unique=True,
        max_length=100,
    )
    url = models.CharField(
        'Ссылка',
        max_length=200,
    )
    state = models.PositiveIntegerField(
        'Положение',
        default=1,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    class MPTTMeta:
        order_insertion_by = ['state']

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
