from ccswm.statApi.models import *
from rest_framework import viewsets
from rest_framework.response import Response
from ccswm.statApi.serializers import *
from rest_framework import permissions
import sqlite3
from django.core import serializers
import json


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


# Custom Views for Raw SQL queries

# Scores
class WinsByNightViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT NightWins.id as ID, NightWins.NightNumber as NightNumber, COUNT(NightWins.TotalWins) as Wins FROM (SELECT c.id, c.nightNumber as NightNumber, r.outcome as TotalWins FROM statApi_results r, statApi_couple c WHERE c.id = r.couple_id AND r.outcome = '1st' ORDER BY NightNumber) as NightWins GROUP BY NightWins.NightNumber''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class WinsByAgeViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT AgeWins.id as ID, AgeWins.ageRange as AgeRange, COUNT(AgeWins.TotalWins) as Wins FROM (SELECT c.id, c.ageRange as ageRange, r.outcome as TotalWins FROM statApi_results r, statApi_couple c WHERE c.id = r.couple_id AND r.outcome = '1st' ORDER BY ageRange) as AgeWins GROUP BY AgeWins.ageRange''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class WinsByMrtlStatViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT MrtlWins.id, MrtlWins.mrtlStat as 'Marital Status', COUNT(MrtlWins.TotalWins) as Wins FROM(SELECT c.id, c.mrtlStat as mrtlStat, r.outcome as TotalWins FROM statApi_results r, statApi_couple c WHERE c.id = r.couple_id AND r.outcome = '1st' ORDER BY mrtlStat) as MrtlWins GROUP BY MrtlWins.mrtlStat''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class AverageWinningScoreViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT id, AVG(totalScore) FROM statApi_results WHERE outcome = "1st"''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class AverageOverallScoreViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT id, AVG(totalScore) FROM statApi_results''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class AverageCoupleVoteViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT Couples.id, (Couples.CoupleA + Couples.CoupleB) / 2 as 'AverageCoupleVote' FROM (SELECT id, AVG(oppAVote) as CoupleA, AVG(oppBVote) as CoupleB FROM statApi_results) as Couples''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class HighestScoreViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT id, totalScore FROM statApi_results ORDER BY totalScore DESC LIMIT 1''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class LowestScoreViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT id, totalScore FROM statApi_results ORDER BY totalScore ASC LIMIT 1''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class HighestLosingScoreViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT id, totalScore FROM statApi_results WHERE outcome != '1st' ORDER BY totalScore DESC LIMIT 1''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class LowestWinningScoreViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT id, totalScore FROM statApi_results WHERE outcome = '1st' ORDER BY totalScore ASC LIMIT 1''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


# Entrees
class EntreeProteinWinnersViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT WinnerTotals.id, WinnerTotals.Protein as Porteins, WinnerTotals.TimesUsed as 'Times Used By Winner' FROM (SELECT e.id, e.protein as Protein, COUNT(e.protein) as TimesUsed FROM statApi_results r, statApi_couple c, statApi_couplemeal m, statApi_entree e WHERE r.couple_id = c.id AND c.coupleMeal_id = m.id AND m.entree_id = e.id AND r.outcome = '1st' GROUP BY Protein) as WinnerTotals ORDER BY WinnerTotals.TimesUsed DESC''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class EntreeProteinOverallViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT OverallTotals.id, OverallTotals.Protein as Porteins, OverallTotals.TimesUsed as 'Times Used Overall' FROM (SELECT e.id, e.protein as Protein, COUNT(e.protein) as TimesUsed FROM statApi_results r, statApi_couple c, statApi_couplemeal m, statApi_entree e WHERE r.couple_id = c.id AND c.coupleMeal_id = m.id AND m.entree_id = e.id GROUP BY Protein) as OverallTotals ORDER BY OverallTotals.TimesUsed DESC''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class EntreeProteinStyleWinnersViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT WinnerTotals.id, WinnerTotals.ProteinStyle as 'Portein Style', WinnerTotals.TimesUsed as 'Times Used By Winner' FROM (SELECT e.id, e.proteinStyle as ProteinStyle, COUNT(e.proteinStyle) as TimesUsed FROM statApi_results r, statApi_couple c, statApi_couplemeal m, statApi_entree e WHERE r.couple_id = c.id AND c.coupleMeal_id = m.id AND m.entree_id = e.id AND r.outcome = '1st' GROUP BY ProteinStyle) as WinnerTotals ORDER BY WinnerTotals.TimesUsed DESC''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class EntreeProteinStyleOverallViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT OverallTotals.id, OverallTotals.ProteinStyle as 'Portein Style', OverallTotals.TimesUsed as 'Times Used Overall' FROM (SELECT e.id, e.proteinStyle as ProteinStyle, COUNT(e.proteinStyle) as TimesUsed FROM statApi_results r, statApi_couple c, statApi_couplemeal m, statApi_entree e WHERE r.couple_id = c.id AND c.coupleMeal_id = m.id AND m.entree_id = e.id GROUP BY ProteinStyle) as OverallTotals ORDER BY OverallTotals.TimesUsed DESC''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class EntreeSideWinnersViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT WinnerTotals.id, WinnerTotals.Side as Sides, WinnerTotals.TimesUsed as 'Times Used By Winner' FROM (SELECT e.id, e.side as Side, COUNT(e.side) as TimesUsed FROM statApi_results r, statApi_couple c, statApi_couplemeal m, statApi_entree e WHERE r.couple_id = c.id AND c.coupleMeal_id = m.id AND m.entree_id = e.id AND r.outcome = '1st' GROUP BY Side) as WinnerTotals ORDER BY WinnerTotals.TimesUsed DESC''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


class EntreeSideOverallViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT OverallTotals.id, OverallTotals.Side as Sides, OverallTotals.TimesUsed as 'Times Used Overall' FROM (SELECT e.id, e.side as Side, COUNT(e.side) as TimesUsed FROM statApi_results r, statApi_couple c, statApi_couplemeal m, statApi_entree e WHERE r.couple_id = c.id AND c.coupleMeal_id = m.id AND m.entree_id = e.id GROUP BY Side) as OverallTotals ORDER BY OverallTotals.TimesUsed DESC''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)


# Starters
class StarterProteinWinnersViewSet(viewsets.ViewSet):
    def list(self, request):
        with sqlite3.connect("./db.sqlite3") as database:
            db = database.cursor()
            queryset = db.execute('''SELECT WinnerTotals.id, WinnerTotals.Protein as Porteins, WinnerTotals.TimesUsed as 'Times Used By Winner' FROM (SELECT s.id, s.protein as Protein, COUNT(s.protein) as TimesUsed FROM statApi_results r, statApi_couple c, statApi_couplemeal m, statApi_starter s WHERE r.couple_id = c.id AND c.coupleMeal_id = m.id AND m.starter_id = s.id AND r.outcome = '1st' GROUP BY Protein) as WinnerTotals ORDER BY WinnerTotals.TimesUsed DESC''')
            results = queryset.fetchall()
        data = json.dumps(results)
        return Response(data)
