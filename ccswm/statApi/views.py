from ccswm.statApi.models import *
from rest_framework import viewsets
from ccswm.statApi.serializers import *
from rest_framework import permissions
import sqlite3


with sqlite3.connect("./db.sqlite3") as database:
    db = database.cursor()


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


class WinsByNightViewSet(viewsets.ModelViewSet):
    queryset = db.execute('''SELECT NightWins.id as ID, NightWins.NightNumber as NightNumber, COUNT(NightWins.TotalWins) as Wins FROM (SELECT c.id, c.nightNumber as NightNumber, r.outcome as TotalWins FROM statApi_results r, statApi_couple c WHERE c.id = r.couple_id AND r.outcome = '1st' ORDER BY NightNumber) as NightWins GROUP BY NightWins.NightNumber''')
    serializer_class = WinsByNightSerializer


class WinsByAgeViewSet(viewsets.ModelViewSet):
    queryset = db.execute('''SELECT AgeWins.id as ID, AgeWins.ageRange as AgeRange, COUNT(AgeWins.TotalWins) as Wins FROM (SELECT c.id, c.ageRange as ageRange, r.outcome as TotalWins FROM statApi_results r, statApi_couple c WHERE c.id = r.couple_id AND r.outcome = '1st' ORDER BY ageRange) as AgeWins GROUP BY AgeWins.ageRange''')
    serializer_class = WinsByAgeSerializer
