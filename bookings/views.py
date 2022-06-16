from home.views import PageTitleViewMixin
from django.views import generic


class BookingsView(PageTitleViewMixin, generic.TemplateView):
    """Displays the Bookings template view"""

    title = "Bookings"
    template_name = "bookings.html"
