from rest_framework import serializers

from apps.restaurant.models import Restaurant, Menu


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("title",)


class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "title", "rating")


class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "title")


class MenuDetailSerializer(serializers.ModelSerializer):
    restaurant = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Menu
        fields = ("title", "price", "restaurant", "count_of_votes")


class MenuUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('title', 'price', 'restaurant')
