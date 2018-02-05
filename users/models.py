# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models


# Create your models here.
from Denarius.Enums import Genres, Roles


class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(_('Nickname'), max_length=30, unique=True)
    full_name = models.CharField(_('Nombre completo'), max_length=80)
    email = models.EmailField(_('Correo electrónico'), unique=True)
    gender = models.IntegerField(_('Genero'), choices=Genres.choices, default=Genres.Male)
    birth_date = models.DateField(_('Fecha de nacimiento'), blank=True, null=True)
    is_active = models.BooleanField(_('Es activa'), default=True)
    register_date = models.DateTimeField(_('Fecha de registro'), auto_now_add=True)
    delete_date = models.DateTimeField(_('Fecha de eliminación'), blank=True, null=True)
    role = models.IntegerField(_('Rol'), choices=Roles.choices, default=Roles.User, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name.split(' ')[0]

    def get_gender(self):
        return Genres.choices[self.gender - 1][1]

    def get_role(self):
        return Roles.choices[self.role - 1][1]
