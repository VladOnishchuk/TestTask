import datetime

from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Max

from apps.restaurant.models import Restaurant, Menu
from apps.restaurant import serializers


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantListSerializer


class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantDetailSerializer


class RestaurantCreateView(APIView):
    def post(self, request):
        request.data['creator'] = request.user.id
        restaurant = serializers.RestaurantCreateSerializer(data=request.data)
        if restaurant.is_valid():
            restaurant.save()
        return Response(status=201)


class MenuListView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuListSerializer


class MenuDetailView(RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuDetailSerializer


class MenuUploadView(APIView):
    def post(self, request):
        for item in request.data:
            item['restaurant'] = Restaurant.objects.get(
                creator__pk=request.user.id
            ).pk
            menu = serializers.MenuUploadSerializer(data=item)
            if menu.is_valid():
                menu.save()
                print("Good")
        return Response(status=201)


class GetTodayMenus(APIView):
    def get(self, request):
        menus = Menu.objects.filter(date=datetime.date.today())
        serializer = serializers.MenuListSerializer(menus, many=True)
        return Response(serializer.data)


class VotingForMenu(APIView):
    def post(self, request, pk):
        menu = Menu.objects.get(pk=pk)
        menu.count_of_votes += 1
        menu.save()
        return Response(status=200)


class ResultToday(APIView):
    def get(self, request):
        final_menu = Menu.objects.filter(date=datetime.date.today()) \
            .order_by('-count_of_votes')[0]
        serializer = serializers.MenuDetailSerializer(final_menu)
        return Response(serializer.data)
