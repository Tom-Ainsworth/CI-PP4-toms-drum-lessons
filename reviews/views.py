from django.shortcuts import render
from django.views import generic
from home.views import PageTitleViewMixin
from .forms import ReviewForm
from .models import Review


class ReviewList(PageTitleViewMixin, generic.ListView):
    title = "Reviews"
    template_name = "reviews.html"

    model = Review
    queryset = Review.objects.filter(approved=True).order_by("created_on")
    paginate_by = 3
