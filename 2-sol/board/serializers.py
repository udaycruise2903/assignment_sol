from rest_framework import serializers
from .models import Category, SubCategory, App, TotalPoints, Task, Screenshot


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = '__all__'


class AppSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subcategory = SubCategorySerializer()

    class Meta:
        model = App
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TotalPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalPoints
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    app = AppSerializer()

    class Meta:
        model = Task
        fields = '__all__'


class ScreenshotSerializer(serializers.ModelSerializer):
    task = TaskSerializer()

    class Meta:
        model = Screenshot
        fields = '__all__'