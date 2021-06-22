# Generated by Django 3.2.3 on 2021-06-22 04:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0011_tags_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='active',
        ),
        migrations.CreateModel(
            name='UsersTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('tag',
                 models.ForeignKey(help_text='Добавленный в избранное рецепт',
                                   on_delete=django.db.models.deletion.CASCADE,
                                   related_name='purchases',
                                   to='recipes.tags',
                                   verbose_name='Тэг')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='userstags',
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользовательский Тэг',
                'verbose_name_plural': 'Пользовательские тэги',
            },
        ),
        migrations.AddConstraint(
            model_name='userstags',
            constraint=models.UniqueConstraint(
                fields=('tag', 'user'), name='unique_usertag'),
        ),
    ]