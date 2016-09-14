from ccswm.statApi.models import Episode, Starter, Entree, Dessert, Entertainment, CoupleMeal, Couple, Results
from rest_framework import viewsets
from ccswm.statApi.serializers import EpisodeSerializer, StarterSerializer, EntreeSerializer, DessertSerializer, EntertainmentSerializer, CoupleMealSerializer, CoupleSerializer, ResultsSerializer


# Create your views here.
class EpisodeViewSet(viewsets.ModelViewSet):
    model = Episode
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class StarterViewSet(viewsets.ModelViewSet):
    model = Starter
    queryset = Starter.objects.all()
    serializer_class = StarterSerializer


class EntreeViewSet(viewsets.ModelViewSet):
    model = Entree
    queryset = Entree.objects.all()
    serializer_class = EntreeSerializer


class DessertViewSet(viewsets.ModelViewSet):
    model = Dessert
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer


class EntertainmentViewSet(viewsets.ModelViewSet):
    model = Entertainment
    queryset = Entertainment.objects.all()
    serializer_class = EntertainmentSerializer


class CoupleMealViewSet(viewsets.ModelViewSet):
    model = CoupleMeal
    queryset = CoupleMeal.objects.all()
    serializer_class = CoupleMealSerializer


class CoupleViewSet(viewsets.ModelViewSet):
    model = Couple
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer


class ResultsViewSet(viewsets.ModelViewSet):
    model = Results
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer

