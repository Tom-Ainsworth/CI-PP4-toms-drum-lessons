from django.views.generic import TemplateView
from home.views import PageTitleViewMixin


class AboutView(PageTitleViewMixin, TemplateView):
    """About page view"""

    template_name = "about.html"
    title = "About"
