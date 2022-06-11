from django.views.generic import TemplateView


# Code from https://www.djangoforge.dev/guides/page-titles/


class PageTitleViewMixin:
    """Mixin used to dynamically add titles to templates"""

    title = ""

    def get_title(self):
        """Returns a title from the object"""
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        title = self.get_title()

        if not title:
            raise ValueError("Fill in the page title")
        context["title"] = self.get_title()
        return context


class HomeView(PageTitleViewMixin, TemplateView):
    """Homepage view"""

    template_name = "home.html"
    title = "Home"
