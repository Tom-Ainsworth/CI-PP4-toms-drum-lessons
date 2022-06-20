from django.shortcuts import render
from django.views import generic, View
from home.views import PageTitleViewMixin
from .forms import ReviewForm
from .models import Review


class ReviewList(PageTitleViewMixin, generic.ListView):
    """List view for displaying user reviews"""

    title = "Reviews"
    template_name = "reviews.html"
    context_object_name = "review_list"

    queryset = Review.objects.filter(approved=True).order_by("created_on")
    paginate_by = 3
