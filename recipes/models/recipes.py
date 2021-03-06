from django.conf import settings
from django.db import models

from .ingredients import Ingredient
from .tags import Tag


class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='recipes',
        help_text='Укажите автора рецепта',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True,
        help_text='Указывается автоматически'
    )
    title = models.CharField(
        verbose_name='Наименование',
        max_length=250,
        help_text='Укажите наименование рецепта',
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=550,
        help_text='Укажите описание рецепта',
    )
    image = models.ImageField(
        verbose_name='Фото',
        help_text='Прикрепите фото рецепта',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэги',
        blank=True,
        related_name='recipes',
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления, мин.',
        help_text='Укажите время приготовления в минутах'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        through_fields=('recipe', 'ingredient'),
        verbose_name='Ингредиенты',
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
