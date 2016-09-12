from ccswm.statApi.models import Episode, Starter, Entree, Dessert, Entertainment, CoupleMeal, Couple, Results
from rest_framework import serializers


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'url', 'season', 'episodeNumber', 'location')


class StarterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Starter
        fields = ('id', 'url', 'protein', 'side')


class EntreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entree
        fields = ('id', 'url', 'protein', 'side')


class DessertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dessert
        fields = ('id', 'url', 'primary', 'secondary')


class EntertainmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entertainment
        fields = ('id', 'url', 'description')


class CoupleMealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoupleMeal
        fields = ('id', 'url', 'starter', 'entree', 'dessert', 'entertainment')


class CoupleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Couple
        fields = ('id', 'url', 'nightNumber', 'ageRange', 'sexPref', 'mrtlStat', 'mrtlLength', 'haveTheme', 'theme', 'foodEth', 'episode', 'coupleMeal')


class ResultsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Results
        fields = ('id', 'url', 'couple', 'oppAVote', 'oppBVote', 'totalScore', 'outcome')
