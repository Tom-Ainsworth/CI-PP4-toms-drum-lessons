from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewList.as_view(), name="reviews"),
    path("create_review", views.CreateReview.as_view(), name="create_review"),
]
