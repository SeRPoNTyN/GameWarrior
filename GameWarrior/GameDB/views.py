from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Createyour views here.


class Home(ListView):
    template_name = "GameDB/index.html"
    model = Game
    context_object_name = "games"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "The Best Games Out There"
        return context


class GetGame(DetailView):
    template_name = "GameDB/single.html"
    model = Game
    context_object_name = "game"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F("views") + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

    def get_queryset(self):
        return Game.objects.filter(slug=self.kwargs["slug"])


class AllGames(ListView):
    template_name = "GameDB/all_games.html"
    model = Game
    context_object_name = "games"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Games"
        return context

    def get_queryset(self):
        return Game.objects.order_by("-views")


class Search(ListView):
    template_name = "GameDB/all_games.html"
    model = Game
    context_object_name = "games"
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Games"
        return context

    def get_queryset(self):
        return Game.objects.filter(title__icontains=self.request.GET.get("s"))
