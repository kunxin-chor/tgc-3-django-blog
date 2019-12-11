
from django.urls import path
from .views import ask_for_donate, donate

urlpatterns = [
    path("ask", ask_for_donate, name="ask"),
    path("donate", donate, name="donate")
]
