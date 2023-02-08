from django.urls import path
from .api_views import ValidateRules

urlpatterns = [
    path("validate", ValidateRules.as_view(), name="Validate Kill Switch"),
]
