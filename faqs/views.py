from home.views import PageTitleViewMixin
from django.views import generic
from .models import Question


class QuestionList(generic.ListView, PageTitleViewMixin):
    """Displays the quesitons in a list view"""

    model = Question
    title = "FAQs"
    template_name = "faqs.html"
    queryset = Question.objects.order_by("-created_on")
