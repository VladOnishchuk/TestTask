from django.urls import path

from apps.restaurant import views

urlpatterns = [
    path("restaurants", views.RestaurantListView.as_view()),
    path("restaurant/<int:pk>", views.RestaurantDetailView.as_view()),
    path("restaurant/create", views.RestaurantCreateView.as_view()),
    path("menus", views.MenuListView.as_view()),
    path("menu/upload", views.MenuUploadView.as_view()),
    path("menus-today", views.GetTodayMenus.as_view()),
    path("voting/<int:pk>", views.VotingForMenu.as_view()),
    path("result-today", views.ResultToday.as_view()),
    path("menu/<int:pk>", views.MenuDetailView.as_view()),
]