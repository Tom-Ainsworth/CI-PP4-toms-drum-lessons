from home.views import PageTitleViewMixin
from django.views import generic


class BookingsView(PageTitleViewMixin, generic.TemplateView):
    """Displays the quesitons in a list view"""

    title = "Bookings"
    template_name = "bookings.html"
