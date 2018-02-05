# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
from users.models import User


class Category(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(_('Nombre'), max_length=60)
    description = models.TextField(_('Descripción'))
    register_date = models.DateField(_('Fecha de registro'), auto_now_add=True)
    delete_date = models.DateField(_('Fecha de eliminación'), blank=True, null=True)
    is_active = models.BooleanField(_('Es activa'), default=True)


class Account(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(_('Nombre'), max_length=60)
    description = models.TextField(_('Descripción'))
    money = models.DecimalField(_('Dinero'), max_digits=12, decimal_places=2)
    register_date = models.DateField(_('Fecha de registro'), auto_now_add=True)
    delete_date = models.DateField(_('Fecha de eliminación'), blank=True, null=True)
    is_active = models.BooleanField(_('Es activa'), default=True)


class Movement(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    account = models.ForeignKey(Account)
    amount = models.DecimalField(_('Monto'), max_digits=12, decimal_places=2)
    type = models.CharField(_('Tipo'), max_length=60)
    date = models.DateField(_('Fecha'))
    concept = models.CharField(_('Concepto'), max_length=100)
    account_transfer = models.IntegerField(blank=True, null=True)
    register_date = models.DateField(_('Fecha de registro'), auto_now_add=True)
    delete_date = models.DateField(_('Fecha de eliminación'), blank=True, null=True)
    is_active = models.BooleanField(_('Es activa'), default=True)
