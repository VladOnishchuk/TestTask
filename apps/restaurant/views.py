import datetime

from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.restaurant.models import Restaurant, Menu
from apps.restaurant import serializers


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantListSerializer


class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantDetailSerializer


class RestaurantCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get_serializer(self):
        return serializers.RestaurantCreateSerializer()

    def post(self, request):
        request.data['creator'] = request.user.id
        restaurant = serializers.RestaurantCreateSerializer(data=request.data)
        if restaurant.is_valid():
            restaurant.save()
        return Response(restaurant.data, status=status.HTTP_201_CREATED)


class MenuListView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuListSerializer


class MenuDetailView(RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuDetailSerializer


class MenuUploadView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get_serializer(self):
        return serializers.MenuUploadSerializer(many=True)

    def post(self, request):
        try:
            for item in request.data:
                item['restaurant'] = Restaurant.objects.get(
                    creator__pk=request.user.id
                ).pk
                menu = serializers.MenuUploadSerializer(data=item)
                if menu.is_valid():
                    menu.save()
        except KeyError as e:
            return Response({
                "message": "Server problem",
                "error": repr(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': "Uploaded"}, status=status.HTTP_201_CREATED)


class GetTodayMenus(APIView):
    def get_serializer(self):
        return serializers.MenuListSerializer()

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
