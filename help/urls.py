from django.urls import path
from django.views.generic import TemplateView

from .views import FindHelpView, ConfirmationView

urlpatterns = [
    # Find help view
    path("find", FindHelpView.as_view(), name="find_help"),
    path("confirm", ConfirmationView.as_view(), name="confirmation"),
]
