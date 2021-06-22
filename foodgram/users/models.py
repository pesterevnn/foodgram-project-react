from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserRole(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'


class UserManager(BaseUserManager):

    def create_user(self, email, username=None, password=None):
        if email is None:
            raise TypeError('User must have an email.')
        if username is None:
            username = email
        user = self.model(email=self.normalize_email(email),
                          username=username)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        if password is None:
            raise TypeError('Superuser must have a password.')
        user = self.create_user(email, username)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    email = models.EmailField('Адрес электронной почты',
                              unique=True,
                              blank=False)
    role = models.CharField('Роль пользователя',
                            choices=UserRole.choices,
                            default=UserRole.USER,
                            max_length=15,
                            )
    objects = UserManager()

    @property
    def is_admin(self):
        return (self.role == UserRole.ADMIN
                or self.is_staff
                or self.is_superuser)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']
