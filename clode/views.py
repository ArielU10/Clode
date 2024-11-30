from rest_framework import viewsets
from .serializer import UsersSerializer, UserPreferencesSerializer, GarmentsSerializer, GarmentTagsSerializer, ExchangeSerializer, ScoresSerializer
from .models import Users, UserPreferences, Garments, GarmentTags, Exchange, Scores

# Create your views here.
class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

class UsersPreferencesView(viewsets.ModelViewSet):
    serializer_class = UserPreferencesSerializer
    queryset = UserPreferences.objects.all()


class GarmentsView(viewsets.ModelViewSet):
    serializer_class = GarmentsSerializer
    queryset = Garments.objects.all()

class GarmentTagsView(viewsets.ModelViewSet):
    serializer_class = GarmentTagsSerializer
    queryset = GarmentTags.objects.all()

class ExchangeView(viewsets.ModelViewSet):
    serializer_class = ExchangeSerializer
    queryset = Exchange.objects.all()

# class ScoresView(viewsets.ModelViewSet):
#     serializer_class = ScoresSerializer
#     queryset = Scores.objects.all()