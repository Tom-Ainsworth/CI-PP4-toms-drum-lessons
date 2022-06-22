from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewList.as_view(), name="reviews"),
    path("create_review", views.CreateReview.as_view(), name="create_review"),
    path("<pk>/update", views.UpdateReview.as_view(), name="update_review"),
    path(
        "delete_review/<int:id>",
        views.CreateReview.delete_review,
        name="delete",
    ),
]
