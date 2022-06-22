from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic, View
from home.views import PageTitleViewMixin
from .forms import ReviewForm
from .models import Review
from django.contrib import messages
from django.urls import reverse_lazy


class ReviewList(PageTitleViewMixin, generic.ListView):
    """List view for displaying user reviews"""

    title = "Reviews"
    template_name = "reviews.html"
    context_object_name = "review_list"
    model = Review

    queryset = Review.objects.filter(approved=True).order_by("created_on")
    paginate_by = 3


class CreateReview(View):
    """Class View to add a new review"""

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "create_review.html",
            {"review_form": ReviewForm()},
        )

    def post(self, request):
        """post the new review to the database"""

        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review_form.instance.author_id = request.user.id
            review_form.save()
        else:
            review_form = ReviewForm()
        messages.success(
            request, "Your review has been created and is pending approval"
        )
        return redirect("reviews")

    def delete_review(request, id):
        review = get_object_or_404(Review, id=id)
        review.delete()
        messages.success(request, "Your review has been deleted.")

        return redirect("reviews")


class UpdateReview(PageTitleViewMixin, generic.UpdateView):
    """Class View to add a new review"""

    title = "Update Review"
    template_name = "update_review.html"
    model = Review

    fields = ["title", "body"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("reviews")
