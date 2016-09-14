from ccswm.statApi.models import *
from rest_framework import viewsets
from ccswm.statApi.serializers import *
from rest_framework import permissions


# Create your views here.
class EpisodeViewSet(viewsets.ModelViewSet):
    model = Episode
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StarterViewSet(viewsets.ModelViewSet):
    model = Starter
    queryset = Starter.objects.all()
    serializer_class = StarterSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EntreeViewSet(viewsets.ModelViewSet):
    model = Entree
    queryset = Entree.objects.all()
    serializer_class = EntreeSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DessertViewSet(viewsets.ModelViewSet):
    model = Dessert
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EntertainmentViewSet(viewsets.ModelViewSet):
    model = Entertainment
    queryset = Entertainment.objects.all()
    serializer_class = EntertainmentSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CoupleMealViewSet(viewsets.ModelViewSet):
    model = CoupleMeal
    queryset = CoupleMeal.objects.all()
    serializer_class = CoupleMealSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CoupleViewSet(viewsets.ModelViewSet):
    model = Couple
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ResultsViewSet(viewsets.ModelViewSet):
    model = Results
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

