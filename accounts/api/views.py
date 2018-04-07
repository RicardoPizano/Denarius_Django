# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Category, Account, Movement
from users.models import User


# Section of categories


@api_view(['GET'])
def view_all_categories(request):
    """
    This function return all categories in the data base
    :param request: petition method GET
    :return: {categories: [{id, user, name, description, register_date, delete_date, is_active}]}
    """
    categories = Category.objects.all().order_by('user')

    response = []

    for category in categories:
        response.append({
            'id': category.pk,
            'user': category.user.get_full_name(),
            'name': category.name,
            'description': category.description,
            'register_date': category.register_date,
            'delete_date': category.delete_date,
            'is_active': category.is_active,
            'category_color': category.category_color
        })

    if response:
        return Response({'categories': response}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def view_user_categories(request, user_id):
    """
    This function return all active categories of a user
    :param request: petition method GET
    :param user_id: id user
    :return: {categories: [{id, name, description}]}
    """
    try:
        user = User.objects.get(pk=user_id)
        categories = Category.objects.filter(user=user, is_active=True).order_by('name')

        response = []

        for category in categories:
            response.append({
                'id': category.pk,
                'name': category.name,
                'description': category.description,
                'category_color': category.category_color
            })

        if response:
            return Response({'categories': response}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_single_category(request, category_id):
    """
    This function return a category
    :param request: petition method GET
    :param category_id: id category
    :return: {category: {id, name, description}}
    """
    try:
        category = Category.objects.get(pk=category_id)

        if category.is_active:

            response = {
                'id': category.pk,
                'name': category.name,
                'description': category.description,
                'category_color': category.category_color
            }

            return Response({'category': response}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@csrf_exempt
def register_category(request):
    """
    This function register a category
    :param request: petition method POST
    :parameter user_id: id user
    :parameter name: category name
    :parameter description: category description
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.data['user_id'])
            name = request.data['name']
            description = request.data['description']
            color = request.data['color']

            Category.objects.create(user=user, name=name, description=description, category_color=color)

            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def update_category(request):
    """
    This function update a category
    :param request: petition method POST
    :parameter category_id: id category
    :parameter name: category name
    :parameter description: category description
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            category = Category.objects.get(pk=request.data['category_id'])
            name = request.data['name']
            description = request.data['description']
            color = request.data['color']

            category.name = name
            category.description = description
            category.category_color = color
            category.save()

            return Response(status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def delete_category(request):
    """
    This function change the attribute from is_active to false and records the date of the operation
    :param request:
    :parameter category_id: id category
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            category = Category.objects.get(pk=request.data['category_id'])

            category.delete_date = datetime.today()
            category.is_active = False

            category.save()

            return Response(status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Section of accounts


@api_view(['GET'])
def view_all_accounts(request):
    """
    This function return all accounts in the data base
    :param request: petition method GET
    :return: {accounts: [{id, user, name, description, money, register_date, delete_date, is_active}]}
    """
    accounts = Account.objects.all().order_by('user')

    response = []

    for account in accounts:
        response.append({
            'id': account.pk,
            'user': account.user.get_full_name(),
            'name': account.name,
            'description': account.description,
            'money': account.money,
            'register_date': account.register_date,
            'delete_date': account.delete_date,
            'is_active': account.is_active
        })

    if response:
        return Response({'accounts': response}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def view_user_accounts(request, user_id):
    """
    This function return all active accounts of a user
    :param request: petition method GET
    :param user_id: id user
    :return: {accounts: [{id, name, description, money}]}
    """
    try:
        user = User.objects.get(pk=user_id)
        accounts = Account.objects.filter(user=user, is_active=True).order_by('name')

        response = []

        for account in accounts:
            response.append({
                'id': account.pk,
                'name': account.name,
                'description': account.description,
                'money': account.money,
            })

        if response:
            return Response({'accounts': response}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_single_account(request, account_id):
    """
    This function return a account
    :param request: petition method GET
    :param account_id: id account
    :return: {account: {id, name, description, money}}
    """
    try:
        account = Account.objects.get(pk=account_id)

        if account.is_active:

            response = {
                'id': account.pk,
                'name': account.name,
                'description': account.description,
                'money': account.money,
            }

            return Response({'account': response}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@csrf_exempt
def register_account(request):
    """
    This function register a account
    :param request: petition method POST
    :parameter user_id: id user
    :parameter name: account name
    :parameter description: account description
    :parameter money: account money
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.data['user_id'])
            name = request.data['name']
            description = request.data['description']
            money = request.data['money']

            Account.objects.create(user=user, name=name, description=description, money=money)

            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def update_account(request):
    """
    This function update a account
    :param request: petition method POST
    :parameter account_id: id account
    :parameter name: account name
    :parameter description: account description
    :parameter money: account money
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            account = Account.objects.get(pk=request.data['account_id'])
            name = request.data['name']
            description = request.data['description']
            money = request.data['money']

            account.name = name
            account.description = description
            account.money = money

            account.save()

            return Response(status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def delete_account(request):
    """
    This function change the attribute from is_active to false and records the date of the operation
    :param request:
    :parameter account_id: id account
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            account = Account.objects.get(pk=request.data['account_id'])

            account.delete_date = datetime.today()
            account.is_active = False

            account.save()

            return Response(status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Section of movements


@api_view(['GET'])
def view_all_movements(request):
    """
    This function return all movements in the data base
    :param request: petition method GET
    :return: {movements: [{id, user, category, account, amount, type, date, concept, account_transfer, register_date,
              delete_date, is_active}]}
    """
    movements = Movement.objects.all().order_by('user')

    response = []

    for movement in movements:
        response.append({
            'id': movement.pk,
            'user': movement.user.get_full_name(),
            'category': movement.category.name,
            'account': movement.account.name,
            'amount': movement.amount,
            'type': movement.type,
            'date': movement.date,
            'concept': movement.concept,
            'account_transfer': movement.account_transfer,
            'register_date': movement.register_date,
            'delete_date': movement.delete_date,
            'is_active': movement.is_active,
        })

    if response:
        return Response({'movements': response}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def view_user_movements(request, user_id):
    """
    This function return all active movements of a user
    :param request: petition method GET
    :param user_id: id user
    :return: {movements: [{id, category, account, amount, type, date, concept, account_transfer}]}
    """
    try:
        user = User.objects.get(pk=user_id)
        movements = Movement.objects.filter(user=user, is_active=True).order_by('date')

        response = []

        for movement in movements:
            response.append({
                'id': movement.pk,
                'category': movement.category.name,
                'account': movement.account.name,
                'amount': movement.amount,
                'type': movement.type,
                'date': movement.date,
                'concept': movement.concept,
                'account_transfer': movement.account_transfer,
            })

        if response:
            return Response({'movements': response}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_single_movement(request, movement_id):
    """
    This function return a movement
    :param request: petition method GET
    :param movement_id: id movement
    :return: {movements: {id, category, account, amount, type, date, concept, account_transfer}}
    """
    try:
        movement = Movement.objects.get(pk=movement_id)

        if movement.is_active:

            response = {
                'id': movement.pk,
                'category': movement.category.name,
                'account': movement.account.name,
                'amount': movement.amount,
                'type': movement.type,
                'date': movement.date,
                'concept': movement.concept,
                'account_transfer': movement.account_transfer,
            }

            return Response({'movement': response}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Movement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@csrf_exempt
def register_movement(request):
    """
    This function register a movement
    :param request: petition method POST
    :parameter user_id: id user
    :parameter category_id: id category
    :parameter account_id: id account
    :parameter amount: movement amount
    :parameter type: movement type
    :parameter date: movement date
    :parameter concept: movement concept
    :parameter account_transfer_id: movement account transfer (can be null)
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.data['user_id'])
            category = Category.objects.get(pk=request.data['category_id'])
            account = Account.objects.get(pk=request.data['account_id'])
            amount = request.data['amount']
            type_movement = request.data['type']
            date = request.data['date']
            concept = request.data['concept']
            account_transfer = request.data['account_transfer_id']

            Movement.objects.create(user=user, category=category, account=account, amount=amount, type=type_movement,
                                    date=date, concept=concept, account_transfer=account_transfer)

            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist or Category.DoesNotExist or Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def update_movement(request):
    """
    This function update a movement
    :param request: petition method POST
    :parameter movement_id: movement id
    :parameter category_id: id category
    :parameter account_id: id account
    :parameter amount: movement amount
    :parameter type: movement type
    :parameter date: movement date
    :parameter concept: movement concept
    :parameter account_transfer_id: movement account transfer (can be null)
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            movement = Movement.objects.get(pk=request.data['movement_id'])
            category = Category.objects.get(pk=request.data['category_id'])
            account = Account.objects.get(pk=request.data['account_id'])
            amount = request.data['amount']
            type_movement = request.data['type']
            date = request.data['date']
            concept = request.data['concept']
            account_transfer = request.data['account_transfer_id']

            movement.category = category
            movement.account = account
            movement.amount = amount
            movement.type = type_movement
            movement.date = date
            movement.concept = concept
            movement.account_transfer = account_transfer

            movement.save()

            return Response(status=status.HTTP_200_OK)
        except Movement.DoesNotExist or Category.DoesNotExist or Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def delete_movement(request):
    """
    This function change the attribute from is_active to false and records the date of the operation
    :param request:
    :parameter movement_id: id movement
    :return: status code 200
    """
    if request.method == 'POST':
        try:
            movement = Movement.objects.get(pk=request.data['movement_id'])

            movement.delete_date = datetime.today()
            movement.is_active = False

            movement.save()

            return Response(status=status.HTTP_200_OK)
        except Movement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
