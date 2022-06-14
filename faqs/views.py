from django.views.generic import TemplateView
from home.views import PageTitleViewMixin


class FaqView(PageTitleViewMixin, TemplateView):
    """FAQs page view"""

    template_name = "faqs.html"
    title = "FAQs"
