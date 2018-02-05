# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User


@api_view(['POST'])
@csrf_exempt
def register_user(request):
    """
    This function register a user
    :param request: petition method POST
    :parameter name: user name
    :parameter email: user email
    :parameter nickname: user nickname
    :parameter password: user password
    :parameter birth_date: user birth date
    :parameter gender: user gender (1 female, 2 male)
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            name = request.data['name']
            email = request.data['email']
            nickname = request.data['nickname']
            password = request.data['password']
            birth_date = request.data['birth_date']
            gender = request.data['gender']

            user = User()
            user.full_name = name
            user.email = email
            user.nickname = nickname
            user.set_password(password)
            user.birth_date = birth_date
            user.gender = gender

            user.save()

            return Response(status=status.HTTP_200_OK)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def delete_user(request):
    """
    This function change the attribute from is_active to false and records the date of the operation
    :param request: petition method POST
    :parameter user_id: id user
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.data['user_id'])

            user.is_active = False
            user.delete_date = datetime.today()

            user.save()

            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def update_user(request):
    """
    This function update a user
    :param request: petition method POST
    :parameter user_id: id user
    :parameter name: user name
    :parameter birth_date: user birth date
    :parameter gender: user gender (1 female, 2 male)
    :return: {user: {id, nickname, full_name, email, gender, birth_date}}
    """
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.data['user_id'])

            name = request.data['name']
            birth_date = request.data['birth_date']
            gender = request.data['gender']

            user.name = name
            user.birth_date = birth_date
            user.gender = gender

            user.save()

            response = {
                'id': user.pk,
                'nickname': user.nickname,
                'full_name': user.get_full_name(),
                'email': user.email,
                'gender': user.get_gender(),
                'birth_date': user.birth_date,
            }

            return Response({'user': response}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_users(request):
    """
    This function return all users in the data base
    :param request: petition method GET
    :return: {users:[{id, last_login, nickname, full_name, short_name, email, gender, birth_date, is_active,
             register_date, delete_date, role}]}
    """
    users = User.objects.all().order_by('-register_date')
    response = []
    for user in users:
        response.append({
            'id': user.pk,
            'last_login': user.last_login,
            'nickname': user.nickname,
            'full_name': user.get_full_name(),
            'short_name': user.get_short_name(),
            'email': user.email,
            'gender': user.get_gender(),
            'birth_date': user.birth_date,
            'is_active': user.is_active,
            'register_date': user.register_date,
            'delete_date': user.delete_date,
            'role': user.get_role()
        })

    if response:
        return Response({'users': response}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)
