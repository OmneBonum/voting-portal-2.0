from django.urls import path, include
from votePortal import views
from rest_framework import routers, viewsets

router = routers.DefaultRouter()
router.register("districts", views.DistrictsView)

urlpatterns = [
    path('', include(router.urls)),
    # token of jwt 
]