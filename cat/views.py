from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Cat


class CatListView(ListView):
    template_name = "cat/cat-list.html"
    model = Cat


class CatDetailView(DetailView):
    template_name = "cat/cat-detail.html"
    model = Cat


class CatCreateView(CreateView):
    template_name = "cat/cat-create.html"
    model = Cat
    fields = ['name','purchaser','cat_type']


class CatUpdateView(UpdateView):
    template_name = "cat/cat-update.html"
    model = Cat
    fields = ['name','purchaser','cat_type']


class CatDeleteView(DeleteView):
    template_name = "cat/cat-delete.html"
    model = Cat
    success_url = reverse_lazy("cat_list")