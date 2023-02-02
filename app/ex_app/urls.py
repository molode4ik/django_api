from rest_framework import routers
from .api import TeaserViewSet
from . import views
from django.urls import path


urlpatterns = [
    path('api/teaser/', views.TeaserView.as_view()),
    path('api/change_teaser_state/', views.WorkTeasersView.as_view())
]
