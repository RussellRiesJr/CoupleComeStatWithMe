from django.db import models

# Create your models here.


seasons = [(number, number) for number in range(1, 5)]
episodes = [(number, number) for number in range(1, 71)]
nights = [(number, number) for number in range(1, 4)]
scores = [(number, number) for number in range(0, 21)]
totals = [(number, number) for number in range(0, 41)]


class Episode(models.Model):
    season = models.IntegerField(choices=seasons, default=1)
    episodeNumber = models.IntegerField(choices=episodes, default=1)
    location = models.CharField(max_length=100)

    def __str__(self):
        return "{}: {}".format(self.id, self.location)


class Starter(models.Model):
    protein = models.CharField(max_length=100)
    proteinStyle = models.CharField(max_length=100, default='')
    side = models.CharField(max_length=100)
    sideStyle = models.CharField(max_length=100, default='')

    def __str__(self):
        return "{}: {}".format(self.id, self.protein)


class Entree(models.Model):
    protein = models.CharField(max_length=100)
    proteinStyle = models.CharField(max_length=100, default='')
    side = models.CharField(max_length=100)
    sideStyle = models.CharField(max_length=100, default='')

    def __str__(self):
        return "{}: {}".format(self.id, self.protein)


class Dessert(models.Model):
    main = models.CharField(max_length=100)
    secondary = models.CharField(max_length=100)

    def __str__(self):
        return "{}: {}".format(self.id, self.primary)


class Entertainment(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return "{}: {}".format(self.id, self.description)


class CoupleMeal(models.Model):
    starter = models.ForeignKey(Starter, related_name='meal')
    entree = models.ForeignKey(Entree, related_name='meal')
    dessert = models.ForeignKey(Dessert, related_name='meal')
    entertainment = models.ForeignKey(Entertainment, related_name='meal')

    def __str__(self):
        return "{}: {}".format(self.id, self.starter.protein)


class Couple(models.Model):
    nightNumber = models.IntegerField(choices=nights, default=1)
    ageRange = models.CharField(max_length=6)
    sexPref = models.CharField(max_length=15)
    mrtlStat = models.CharField(max_length=15)
    mrtlLength = models.CharField(max_length=15)
    theme = models.CharField(max_length=30)
    foodEth = models.CharField(max_length=30)
    episode = models.ForeignKey(Episode, related_name='couple')
    coupleMeal = models.ForeignKey(CoupleMeal, related_name='couple')

    def __str__(self):
        return "{}: {}".format(self.id, self.nightNumber)


class Results(models.Model):
    couple = models.ForeignKey(Couple, related_name='results')
    oppAVote = models.IntegerField(choices=scores, default=0)
    oppBVote = models.IntegerField(choices=scores, default=0)
    totalScore = models.IntegerField(choices=totals, default=0)
    outcome = models.CharField(max_length=15)

