from django.views.generic import DetailView
from .models import Page


class IndexView(DetailView):
    model = Page
    template_name = 'app/index.html'
