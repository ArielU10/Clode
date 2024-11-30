from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = '__all__'

class GarmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garments
        fields = '__all__'

class GarmentTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GarmentTags
        fields = '__all__'

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'

# class ScoresSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Scores
#         fields = '__all__'