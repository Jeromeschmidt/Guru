from django.urls import path
from django.views.generic import TemplateView

from .views import FindHelpView, ConfirmationView, MatchView

urlpatterns = [
    # Find help view
    path("find", FindHelpView.as_view(), name="find_help"),
    path("match", MatchView.as_view(), name="match"),
    path("confirm", ConfirmationView.as_view(), name="confirmation"),
]
