from statApi.models import Episode, Starter, Entree, Dessert, Entertainment, CoupleMeal, Couple, Results
from rest_framework import viewsets
from statApi.serializers import EpisodeSerializer, StarterSerializer, EntreeSerializer, DessertSerializer, EntertainmentSerializer, CoupleMealSerializer, CoupleSerializer, ResultsSerializer


# Create your views here.
class EpisodeList(viewsets.ModelViewSet):
    model = Episode
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class StarterList(viewsets.ModelViewSet):
    model = Starter
    queryset = Starter.objects.all()
    serializer_class = StarterSerializer


class EntreeList(viewsets.ModelViewSet):
    model = Entree
    queryset = Entree.objects.all()
    serializer_class = EntreeSerializer


class DessertList(viewsets.ModelViewSet):
    model = Dessert
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer


class EntertainmentList(viewsets.ModelViewSet):
    model = Entertainment
    queryset = Entertainment.objects.all()
    serializer_class = EntertainmentSerializer


class CoupleMealList(viewsets.ModelViewSet):
    model = CoupleMeal
    queryset = CoupleMeal.objects.all()
    serializer_class = CoupleMealSerializer


class CoupleList(viewsets.ModelViewSet):
    model = Couple
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer


class ResultsList(viewsets.ModelViewSet):
    model = Results
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
