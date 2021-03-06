"""ccswm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from ccswm.statApi import views


router = routers.DefaultRouter()
router.register(r'episodes', views.EpisodeViewSet)
router.register(r'starters', views.StarterViewSet)
router.register(r'entrees', views.EntreeViewSet)
router.register(r'desserts', views.DessertViewSet)
router.register(r'entertainment', views.EntertainmentViewSet)
router.register(r'couple_meal', views.CoupleMealViewSet)
router.register(r'couples', views.CoupleViewSet)
router.register(r'results', views.ResultsViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^winsby/night', views.WinsByNightViewSet.as_view({'get': 'list'})),
    url(r'^winsby/age', views.WinsByAgeViewSet.as_view({'get': 'list'})),
    url(r'^winsby/mrtlstat', views.WinsByMrtlStatViewSet.as_view({'get': 'list'})),
    url(r'^scores/avgwin', views.AverageWinningScoreViewSet.as_view({'get': 'list'})),
    url(r'^scores/avgoverall', views.AverageOverallScoreViewSet.as_view({'get': 'list'})),
    url(r'^scores/avgcouple', views.AverageCoupleVoteViewSet.as_view({'get': 'list'})),
    url(r'^scores/highest', views.HighestScoreViewSet.as_view({'get': 'list'})),
    url(r'^scores/lowest', views.LowestScoreViewSet.as_view({'get': 'list'})),
    url(r'^scores/highlosing', views.HighestLosingScoreViewSet.as_view({'get': 'list'})),
    url(r'^scores/lowwinning', views.LowestWinningScoreViewSet.as_view({'get': 'list'})),
    url(r'^entree/proteinwinners', views.EntreeProteinWinnersViewSet.as_view({'get': 'list'})),
    url(r'^entree/proteinoverall', views.EntreeProteinOverallViewSet.as_view({'get': 'list'})),
    url(r'^entree/proteinstylewinners', views.EntreeProteinStyleWinnersViewSet.as_view({'get': 'list'})),
    url(r'^entree/proteinstyleoverall', views.EntreeProteinStyleOverallViewSet.as_view({'get': 'list'})),
    url(r'^entree/sidewinners', views.EntreeSideWinnersViewSet.as_view({'get': 'list'})),
    url(r'^entree/sideoverall', views.EntreeSideOverallViewSet.as_view({'get': 'list'})),
    url(r'^starter/proteinwinners', views.StarterProteinWinnersViewSet.as_view({'get': 'list'})),
    url(r'^starter/proteinoverall', views.StarterProteinOverallViewSet.as_view({'get': 'list'})),
    url(r'^starter/sidewinners', views.StarterSideWinnersViewSet.as_view({'get': 'list'})),
    url(r'^starter/sideoverall', views.StarterSideOverallViewSet.as_view({'get': 'list'})),
    url(r'^starter/proteinstylewinners', views.StarterProteinStyleWinnersViewSet.as_view({'get': 'list'})),
    url(r'^starter/proteinstyleoverall', views.StarterProteinStyleOverallViewSet.as_view({'get': 'list'})),
    url(r'^dessert/mainwinners', views.DessertMainWinnersViewSet.as_view({'get': 'list'})),
    url(r'^dessert/mainoverall', views.DessertMainOverallViewSet.as_view({'get': 'list'})),
    url(r'^dessert/secondarywinners', views.DessertSecondaryWinnersViewSet.as_view({'get': 'list'})),
    url(r'^dessert/secondaryoverall', views.DessertSecondaryOverallViewSet.as_view({'get': 'list'})),
]

