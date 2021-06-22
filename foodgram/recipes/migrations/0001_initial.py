# Generated by Django 3.2.3 on 2021-05-31 07:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранный рецепт',
                'verbose_name_plural': 'Избранные рецепты',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
                'ordering': ['subscriber'],
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title',
                 models.CharField(db_index=True,
                                  help_text='Укажите наименование ингридиента',
                                  max_length=150,
                                  verbose_name='Наименование')),
                ('dimension',
                 models.CharField(help_text='Укажите единицу измерения',
                                  max_length=20,
                                  verbose_name='Ед. изм.')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Ingredients_Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Ингредиент для рецепта',
                'verbose_name_plural': 'Ингредиенты для рецепта',
                'ordering': ['ingredient'],
            },
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
                'ordering': ['customer'],
            },
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date',
                 models.DateTimeField(auto_now_add=True,
                                      db_index=True,
                                      help_text='Указывается автоматически',
                                      verbose_name='Дата публикации')),
                ('title',
                 models.CharField(help_text='Укажите наименование рецепта',
                                  max_length=250,
                                  verbose_name='Наименование')),
                ('description',
                 models.CharField(help_text='Укажите описание рецепта',
                                  max_length=550,
                                  verbose_name='Описание')),
                ('image', models.ImageField(
                    help_text='Прикрепите фото рецепта', upload_to='', verbose_name='Фото')),
                ('cooking_time', models.PositiveIntegerField(
                    help_text='Укажите время приготовления в минутах', verbose_name='Время приготовления, мин.')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(choices=[
                 ('B', 'breakfast'), ('L', 'lunch'), ('D', 'dinner')], max_length=1, verbose_name='Таг')),
                ('description', models.CharField(blank=True,
                 max_length=50, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.AddConstraint(
            model_name='tags',
            constraint=models.UniqueConstraint(
                fields=('tag',), name='unique_tag'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='author',
            field=models.ForeignKey(
                help_text='Укажите автора рецепта',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='recipes',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.ManyToManyField(
                through='recipes.Ingredients_Recipe',
                to='recipes.Ingredients',
                verbose_name='Ингредиенты'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='tags',
            field=models.ManyToManyField(
                blank=True,
                related_name='recipes',
                to='recipes.Tags',
                verbose_name='Тэги'),
        ),
        migrations.AddField(
            model_name='purchases',
            name='customer',
            field=models.ForeignKey(
                help_text='Тот кто включает в список покупок',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='customer',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='purchases',
            name='recipe',
            field=models.ForeignKey(
                help_text='Добавленный в избранное рецепт',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='purchases',
                to='recipes.recipes',
                verbose_name='Рецепт'),
        ),
        migrations.AddField(
            model_name='ingredients_recipe',
            name='ingredient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='recipes.ingredients',
                verbose_name='Ингредиент'),
        ),
        migrations.AddField(
            model_name='ingredients_recipe',
            name='recipe',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='recipes.recipes'),
        ),
        migrations.AddField(
            model_name='follows',
            name='author',
            field=models.ForeignKey(
                help_text='Тот на кого подписываются',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='following',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='follows',
            name='subscriber',
            field=models.ForeignKey(
                help_text='Тот кто подписывается',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='subscriber',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Подписчик'),
        ),
        migrations.AddField(
            model_name='favoriterecipes',
            name='recipe',
            field=models.ForeignKey(
                help_text='Добавленный в избранное рецепт',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='favorite_recipes',
                to='recipes.recipes',
                verbose_name='Рецепт'),
        ),
        migrations.AddField(
            model_name='favoriterecipes',
            name='user',
            field=models.ForeignKey(
                help_text='Тот кто включает в избранное',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='user',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Пользователь'),
        ),
        migrations.AddConstraint(
            model_name='purchases',
            constraint=models.UniqueConstraint(
                fields=('customer', 'recipe'), name='unique_purchase'),
        ),
        migrations.AddConstraint(
            model_name='follows',
            constraint=models.UniqueConstraint(
                fields=('subscriber', 'author'), name='unique_follow'),
        ),
        migrations.AddConstraint(
            model_name='favoriterecipes',
            constraint=models.UniqueConstraint(
                fields=('user', 'recipe'), name='unique_favorite_recipe'),
        ),
    ]
