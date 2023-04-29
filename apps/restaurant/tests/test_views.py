import datetime

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.restaurant.models import Restaurant, Menu
@pytest.mark.django_db
@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.mark.django_db
@pytest.fixture
def restaurant(user, db):
    return Restaurant.objects.create(title='Test Restaurant', rating='5', creator=user)

@pytest.mark.django_db
@pytest.fixture
def menu(restaurant, db):
    return Menu.objects.create(
        title='Test Menu',
        date=datetime.date.today(),
        restaurant=restaurant,
        count_of_votes=0,
        price=100
    )



@pytest.fixture
def api_client():
    return APIClient()


def test_list_restaurants(api_client, restaurant):
    url = reverse('restaurant-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


def test_retrieve_restaurant(api_client, restaurant):
    url = reverse('restaurant-detail', args=[restaurant.pk])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == restaurant.title


def test_create_restaurant(api_client, user):
    url = reverse('restaurant-create')
    data = {'title': 'New Restaurant', 'rating': 4, 'creator': user.pk}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


def test_list_menus(api_client, menu):
    url = reverse('menu-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['title'] == menu.title


def test_retrieve_menu(api_client, menu):
    url = reverse('menu-detail', args=[menu.pk])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == menu.title



def test_get_today_menus(api_client, menu):
    url = reverse('get-today-menus')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == menu.title


def test_vote_for_menu(api_client, menu):
    url = reverse('voting-for-menu', args=[menu.pk])
    response = api_client.post(url)
    assert response.status_code == status.HTTP_200_OK
    assert Menu.objects.first().count_of_votes == 1


def test_get_result_today(api_client, menu):
    url = reverse('result-today')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == menu.title
    assert response.data['count_of_votes'] == 0