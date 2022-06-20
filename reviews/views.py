from django.shortcuts import redirect, render
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


class CreateReview(PageTitleViewMixin, View):
    """Class View to add a new review"""

    title = "Create Review"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "create_review.html",
            {"review_form": ReviewForm()},
        )

    def post(self, request, *args, **kwargs):
        """post the new review to the database"""

        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review_form.instance.author_id = request.user.id
            review_form.save()
        else:
            review_form = ReviewForm()

        return redirect("reviews")
