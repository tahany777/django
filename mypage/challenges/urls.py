from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),
    ##Dynamic path
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]

# Dynamic path segments and captured values
