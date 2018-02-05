# -*- coding: utf-8 -*-
from djchoices import DjangoChoices, ChoiceItem


class Roles(DjangoChoices):
    Admin = ChoiceItem(1, 'Administrador')
    User = ChoiceItem(2, 'Usuario')


class Genres(DjangoChoices):
    Female = ChoiceItem(1, 'Femenino')
    Male = ChoiceItem(2, 'Masculino')
