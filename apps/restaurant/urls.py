from django.urls import path

from apps.restaurant import views

urlpatterns = [
    path("restaurants", views.RestaurantListView.as_view(), name='restaurant-list'),
    path("restaurant/<int:pk>", views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path("restaurant/create", views.RestaurantCreateView.as_view(), name='restaurant-create'),
    path("menus", views.MenuListView.as_view(), name='menu-list'),
    path("menu/<int:pk>", views.MenuDetailView.as_view(), name='menu-detail'),
    path("menu/upload", views.MenuUploadView.as_view(), name='menu-upload'),
    path("menus-today", views.GetTodayMenus.as_view(), name='get-today-menus'),
    path("voting/<int:pk>", views.VotingForMenu.as_view(), name='voting-for-menu'),
    path("result-today", views.ResultToday.as_view(), name='result-today'),
]
