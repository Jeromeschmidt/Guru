from django.urls import path
from django.views.generic import TemplateView

from .views import FindHelpView

urlpatterns = [
    # Find help view
    path("find", FindHelpView.as_view(), name="find_help"),
]
