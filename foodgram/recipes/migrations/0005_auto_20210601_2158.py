# Generated by Django 3.2.3 on 2021-06-01 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0004_alter_favoriterecipes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriterecipes',
            name='recipe',
            field=models.ForeignKey(help_text='Добавленный в избранное рецепт', on_delete=django.db.models.deletion.CASCADE, related_name='favorite_authors', to='recipes.recipes', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='favoriterecipes',
            name='user',
            field=models.ForeignKey(help_text='Тот кто включает в избранное', on_delete=django.db.models.deletion.CASCADE, related_name='favorite_recipes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
