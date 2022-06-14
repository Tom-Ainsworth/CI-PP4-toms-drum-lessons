from django.urls import path
from . import views


urlpatterns = [
    path("", views.FaqView.as_view(), name="faqs"),
]
